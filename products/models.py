from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings



class Category(models.Model):
    category_name = models.CharField(max_length = 200)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if self.slug is not None:
            self.slug = slugify(self.category_name)

        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:home', kwargs={'category_slug':self.slug})



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    img = models.ImageField(upload_to="media/products_images/", null=True, blank=True)
    product_name = models.CharField(max_length = 200)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def get_final_price(self):
        if self.discount_price:
        
            return self.price - self.discount_price

        return self.price

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={'slug' : self.slug})

    def get_add_to_cart(self):
        return reverse("products:add-to-cart", kwargs={'slug': self.slug})

    def remove_item_from_cart(self):
        return reverse("products:remove-item-from-cart", kwargs={'slug' : self.slug})

    def remove_single_item_from_cart(self):
        return reverse("products:remove_single_item_from_cart", kwargs={'slug':self.slug})




class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.product_name

    def get_total_item_price(self):
        return self.item.price * self.quantity

    def get_total_discount_item_price(self):
        return self.item.discount_price * self.quantity

    def get_total_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_total_price(self):
        if self.item.discount_price:
            return self.get_total_amount_saved()

        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()


    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for item in self.items.all():
            total = total + item.get_total_price()
            return total



