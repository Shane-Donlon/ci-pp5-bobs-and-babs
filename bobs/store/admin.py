from django.contrib import admin

from .models import Customer, Order, OrderItems, Product, ShippingInformation

# Register your models here.

@admin.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone", "email", "registration_date"]
    search_fields = ["first_name", "email", "phone"]
