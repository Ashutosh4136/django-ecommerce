from . import views
from django.urls import path

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    # Cart URLs
    path('cart/view/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/increment/<int:product_id>/', views.increment_cart_item, name='increment_cart_item'),
    path('cart/decrement/<int:product_id>/', views.decrement_cart_item, name='decrement_cart_item'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
    path('cart/delete/<int:product_id>/', views.delete_cart_item, name='cart_delete'),

    # Checkout + Search + Catalog + Orders
    path('checkout/', views.checkout, name='checkout'),
    path('search/', views.search_products, name='search_products'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('order/<int:order_id>/confirm/', views.confirm_delivery, name='confirm_delivery'),

    #Wishlist part
    path('wishlist/', views.wishlist_view, name='wishlist_view'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),

]
