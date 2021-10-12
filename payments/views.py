from django.shortcuts import render, redirect, get_object_or_404
import razorpay
from django.conf import settings
from products.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


razorpay_client = razorpay.Client(auth=(settings.CLIENT_KEY_ID, settings.CLIENT_KEY_SECRET))


@login_required
def checkout(request, slug):
    product = get_object_or_404(Product, slug=slug)

    amount = product.get_final_price() * 100
    currency = 'INR'

    razorpay_order = razorpay_client.order.create(dict(
        amount = amount,
        currency = currency,
        payment_capture = '0'
    ))

    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['merchant_key'] = settings.CLIENT_KEY_ID
    context['amount'] = amount
    context['currence'] = currency
    context['callback_url'] = callback_url
    context['product'] = product


    return render(request, "payments/payment.html", context)


@csrf_exempt
def paymenthandler(request):
    pass


