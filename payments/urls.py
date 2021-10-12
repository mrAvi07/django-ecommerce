from django.urls import path 
from .views import checkout


app_name = 'payments'


urlpatterns = [
    path('checkout/<slug>', checkout, name="checkout"),
]