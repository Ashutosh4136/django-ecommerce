from django.shortcuts import render

# Create your views here.
# checkout/views.py
from django.shortcuts import render

def checkout_view(request):
    cart = request.session.get('cart', {})
    # For now, just show confirmation
    return render(request, 'checkout/checkout.html')
