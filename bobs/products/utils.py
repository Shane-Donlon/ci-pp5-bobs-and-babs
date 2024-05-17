# Description: Utility functions for products app
from typing import Type

from .models import Product


def verify_quantity_in_cart(product: Type[Product], quantity_in_cart: int) -> bool:

    if (quantity_in_cart > product.max_quantity) or (quantity_in_cart < 0):
        return False
    return True

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
