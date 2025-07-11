# Create your views here.
from django.shortcuts import redirect, render
from .models import CartItem, models
from .models import Product, Category,Review,Wishlist
from django.shortcuts import render, get_object_or_404
from .forms import ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CheckoutForm
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def landing_page(request):
    categories = Category.objects.all()
    featured_products = Product.objects.all().order_by('-id')[:6]  # latest 6 products

    return render(request, 'store/landing.html', {
        'categories': categories,
        'featured_products': featured_products
    })


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()
    avg_rating = reviews.aggregate(models.Avg('rating'))['rating__avg']
    form = ReviewForm()

    # Handle review form POST
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', product_id=product.id)

    return render(request, 'store/product_detail.html', {
        'product': product,
        'form': form,
        'reviews': reviews,
        'avg_rating': avg_rating,
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})



@login_required
def increment_cart_item(request, product_id):
    item = get_object_or_404(CartItem, user=request.user, product_id=product_id)
    item.quantity += 1
    item.save()
    return redirect('view_cart')

@login_required
def decrement_cart_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.filter(user=request.user, product=product).first()

    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()  # only delete when quantity is already 1

    return redirect('view_cart')


@login_required
def delete_cart_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.filter(user=request.user, product=product).first()

    if cart_item:
        cart_item.delete()

    return redirect('view_cart')


@login_required
def remove_from_cart(request, product_id):
    item = get_object_or_404(CartItem, user=request.user, product_id=product_id)
    item.delete()
    return redirect('view_cart')

@login_required
def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    return redirect('view_cart')



def checkout(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
    
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    order = Order.objects.create(
        user=request.user,
        full_name=full_name,
        address=address,
        phone=phone,
        total_price=total_price,
        created_at=timezone.now()
    )


    for product_id_str, quantity in cart.items():
        try:
            product = Product.objects.get(id=int(product_id_str))
            item_total = product.price * quantity
            total_price += item_total
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total,
            })
        except Product.DoesNotExist:
            continue

    return render(request, 'store/checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def search_products(request):
    query = request.GET.get('query')
    products = Product.objects.filter(title__icontains=query) if query else []

    return render(request, 'store/search_results.html', {
        'query': query,
        'products': products
    })

def catalog_view(request):
    category_slug = request.GET.get('category')
    categories = Category.objects.all()

    if category_slug:
        products = Product.objects.filter(category__slug=category_slug)
    else:
        products = Product.objects.all()

    return render(request, 'store/catalog.html', {
        'products': products,
        'categories': categories,
        'selected_category': category_slug
    })


@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    products = []
    total_price = 0

    for product_id_str, quantity in cart.items():
        try:
            product = Product.objects.get(id=int(product_id_str))
            products.append({'product': product, 'quantity': quantity})
            total_price += product.price * quantity
        except Product.DoesNotExist:
            continue

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                full_name=form.cleaned_data['full_name'],
                address=form.cleaned_data['address'],
                phone=form.cleaned_data['phone'],
                total_price=total_price
            )
            for item in products:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity']
                )
            # Clear cart after successful order
            request.session['cart'] = {}
            return render(request, 'store/order_success.html', {'order': order})
    else:
        form = CheckoutForm()

    return render(request, 'store/checkout.html', {
        'form': form,
        'products': products,
        'total_price': total_price
    })

@login_required
def confirm_delivery(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if order.status != 'delivered':
        messages.error(request, "Order cannot be confirmed unless it's marked as delivered.")
    elif order.status == 'confirmed':
        messages.info(request, "Order is already confirmed.")
    else:
        order.status = 'confirmed'
        order.confirmed_at = timezone.now()
        order.save()
        messages.success(request, "✅ Thank you for confirming delivery.")

    return redirect('order_detail', order_id=order.id)



@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist_view')

@login_required
def remove_from_wishlist(request, product_id):
    Wishlist.objects.filter(user=request.user, product_id=product_id).delete()
    return redirect('wishlist_view')

@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'store/wishlist.html', {'wishlist_items': wishlist_items})
