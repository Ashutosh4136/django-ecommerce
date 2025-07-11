from .models import Category,Product

def categories_processor(request):
    return {
        'categories': Category.objects.all(),
        'products_nav': Product.objects.all(),
    }
