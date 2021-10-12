from django.urls import path
from .views import (
    product_list,
    product_detail,
    order_summary,
    add_to_cart,
    remove_item_from_cart,
    remove_single_item_from_cart,
    contact,
)

app_name = 'products'

urlpatterns = [
    path('', product_list, name="home"),
    path('product-detail/<slug>/', product_detail, name="detail"),
    path('order-summary/', order_summary, name="order-summary"),
    path('add-to-cart/<slug>/', add_to_cart, name="add-to-cart"),
    path('remove-item-from-cart/<slug>/', remove_item_from_cart, name="remove-item-from-cart"),
    path('remove_single_item_from_cart/<slug>/',remove_single_item_from_cart, name="remove_single_item_from_cart"),
    path('contact/', contact, name="contact")
]
