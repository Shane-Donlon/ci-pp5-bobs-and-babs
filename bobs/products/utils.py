# Description: Utility functions for products app
from typing import Type

from django.http import HttpRequest

from .models import Order, Product


def verify_quantity_in_cart(
    product: Type[Product],
    quantity_in_cart: int
) -> bool:

    if (quantity_in_cart > product.max_quantity) or (quantity_in_cart < 0):
        return False
    return True


def create_plural_string(product_name: str) -> str:
    last_char = product_name[-1]
    if last_char != "s":
        return f"{product_name}s"
    return f"{product_name}"


def get_plural_string(quantity: int, product: Type[Product]) -> str:
    # return the correct name of the product avoids "Doughnutss" plural
    last_char = product.name[-1]
    if quantity == 1 and last_char != "s":
        return product.name
    if quantity == 1 and last_char == "s":
        return product.name[:-1]
    if quantity > 1 and last_char != "s":
        return f"{product.name}s"
    return f"{product.name}"


def check_order_item(quantity: int, max_quantity: int) -> bool:
    if quantity > max_quantity:
        return False
    return True


def authenticated_users(request: Type[HttpRequest]) -> Type[Order]:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer,
                                                 complete=False)
    order.save()
    return order


def un_authenticated_users_no_session(
    request: Type[HttpRequest]
) -> Type[Order]:
    request.session.create()
    request.session["customer"] = request.session.session_key
    order, created = Order.objects.get_or_create(
        transaction_id=request.session["customer"],
        customer=None,
        complete=False)
    order.save()
    return order


def un_authenticated_order_complete(request: Type[HttpRequest]) -> Type[Order]:
    request.session.cycle_key()
    request.session["customer"] = request.session.session_key
    order, created = Order.objects.get_or_create(
        transaction_id=request.session["customer"],
        customer=None,
        complete=False)
    order.save()
    return order
