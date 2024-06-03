import uuid

from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.CharField(max_length=300, null=True, blank=False)
    town = models.CharField(max_length=60, null=True, blank=False)
    county = models.CharField(max_length=60, null=True, blank=False)
    eircode = models.CharField(max_length=8, null=True, blank=False,)
    phone = models.CharField(max_length=60, null=True, blank=False)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=False, auto_now_add=False, null=True,)

    def __str__(self) -> str:
        return f"{self.user}"


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    sku = models.CharField(max_length=200, default=uuid.uuid4, unique=True, editable=False)
    image = CloudinaryField('image', null=True, blank=False)
    image_description = models.CharField(max_length=200, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, editable=False)
    max_quantity = models.IntegerField(default=10, null=True, blank=False)
    contains_allergin = models.ManyToManyField("Allergin", blank=True,  related_name="contains")
    may_contain_allergin = models.ManyToManyField("Allergin", blank=True, related_name="may_contain")
    showing_in_shop = models.BooleanField(default=True, null=True, blank=False)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)




class Allergin(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False, unique=True)
    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name_plural = "Allergins"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True, blank=True)
    delivery = models.BooleanField(default=False, null=True, blank=False)
    delivery_fee = models.FloatField(default=4, null=True, blank=False)
    cart_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fulfilled = models.BooleanField(default=False, null=True, blank=False)


    def __str__(self):
        return str(self.transaction_id)

    def get_cart_total(self):
        orderitems = self.orderitems_set.all()
        total = sum([item.get_sub_total for item in orderitems])
        if self.delivery:
            total += self.delivery_fee

        return total

class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(default=0, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_sub_total(self):
        return self.product.price * self.quantity



    class Meta:
        verbose_name_plural = "Order Items"
    def __str__(self) -> str:
        return self.product.name

class ShippingInformation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=200, null=True, blank=False)
    last_name = models.CharField(max_length=200, null=True, blank=False)
    email = models.EmailField(max_length=200, null=True, blank=False)
    address = models.CharField(max_length=300, null=True, blank=False)
    town = models.CharField(max_length=60, null=True, blank=False)
    county = models.CharField(max_length=60, null=True, blank=False)
    eircode = models.CharField(max_length=8, null=True, blank=False)
    phone = models.CharField(max_length=12, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Shipping Information"

    def __str__(self) -> str:
        return f"{self.address}"
