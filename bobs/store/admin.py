from django.contrib import admin

from .models import Customer, Order, OrderItems, Product, ShippingInformation

# Register your models here.

@admin.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone", "email", "registration_date"]
    search_fields = ["first_name", "email", "phone"]

@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    search_fields = ["name", "sku", ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "transaction_id"]
    search_fields = ["customer", "transaction_id", ]
    
@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity"]
    search_fields = ["product", "quantity"]
