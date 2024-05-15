from django.contrib.auth.models import User
from django.db import models


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
    last_login = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return f"{self.user}"


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    sku = models.CharField(max_length=200, null=True, blank=False, unique=True)
    image = models.ImageField(null=True, blank=False, )
    image_description = models.CharField(max_length=200, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    allergin_info = models.TextField(null=True, blank=False)
    def __str__(self) -> str:
        return f"{self.name}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    delivery = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return str(self.transaction_id)

class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Order Items"
    def __str__(self) -> str:
        return self.product.name

class ShippingInformation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=300, null=True, blank=False)
    town = models.CharField(max_length=60, null=True, blank=False)
    county = models.CharField(max_length=60, null=True, blank=False)
    eircode = models.CharField(max_length=8, null=True, blank=False)
    phone = models.CharField(max_length=60, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Shipping Information"

    def __str__(self) -> str:
        return f"{self.address}"
