from django.contrib import admin
from .models import Product, Category, OrderItem, Order


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(Order)
