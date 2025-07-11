# Register your models here.
from django.contrib import admin
from .models import Category, Product,Review,Order

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'created_at']
    list_filter = ['status']
    ordering = ['-created_at']

