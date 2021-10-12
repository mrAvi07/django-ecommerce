from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import Product, Order, OrderItem, Category
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from .forms import ContactForm
from .helper import ContactFormView



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'categories': categories,
        'products': products,
        'category': category,
    }
    return render(request, "products/home.html", context)



class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"

product_detail = ProductDetailView.as_view()



class OrderSummary(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            orders = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'orders' : orders,
            }
            return render(self.request, 'products/order_summary.html', context)

        except ObjectDoesNotExist:
            return render(self.request, 'products/order_summary.html')

order_summary = OrderSummary.as_view()



@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)

    order_item, created = OrderItem.objects.get_or_create(
        item = item,
        user=request.user,
        ordered = False,
    )

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
            return redirect("products:order-summary")
        else:
            messages.info(request, "This item was added to your cart")
            order.items.add(order_item)
            return redirect("products:order-summary")
    else:


        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user,
            ordered_date=ordered_date
        )
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
        return redirect('products:order-summary')


@login_required
def remove_item_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            order.save()
            return redirect('products:order-summary')
        else:
            messages.info(request, "This item is not in your cart")
            return redirect('products:order-summary')

    else:
        messages.info(request, "You haven't any active order")
        return redirect('products:home')



@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.get(item=item, user=request.user, ordered=False)
            if order_item.quantity > 1:
                order_item.quantity-= 1
                order_item.save()
                messages.info(request, "Quantity was updated succfully!")
                return redirect("products:order-summary")

            else:
                order.items.remove(order_item)
                messages.info(request, "Order Item was removed!")
                return redirect("products:order-summary")


        else:
            messages.info(request, "This item is not in your cart")
            return redirect("products:order-summary")

    else:
        messages.info(request, "You not have an active order!")
        return redirect("products:home")




class ContactView(ContactFormView):
    form_class = ContactForm


contact = ContactView.as_view()


