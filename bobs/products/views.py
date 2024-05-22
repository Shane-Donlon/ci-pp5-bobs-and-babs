import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from . import utils
from .models import Order, OrderItems, Product

# Create your views here.


class ProductsPageDefaultView(View):

    def get(self, request):
        products = Product.objects.all()
        context = {
            "products": products
        }

        return render(request, "products/products.html",context )


class ProductDetailView(View,):
    def get(self, request, slug_field):
        product = get_object_or_404(Product, slug=slug_field)
        allergens = product.allergin_info.split('\n')
        contains = allergens[0].split(":")[1].split(",")
        may_contain = allergens[1].split(":")[1].split(",")




        context = {
            "product": product,
            "contains": contains,
            "may_contain": may_contain,

        }
        return render(request, "products/product.html", context)


class AddToCart(View):

    def post(self, request, slug_field):

        if request.user.is_authenticated:
            # if user is authenticated get or create an order
            # if the order is complete create a new order
            order = utils.authenticated_users(request)
        if not request.user.is_authenticated:
            # if the user is not authenticated set customer to none
            # and create a session key to identify the order transaction
            # if the order is complete create a new order
            if not request.session.get("customer"):
                order = utils.un_authenticated_users_no_session(request)

            if request.session.get("customer"):
                order = Order.objects.get(transaction_id=request.session.get("customer"))
                if order.complete:
                    order = utils.un_authenticated_order_complete(request)

        post_data = json.loads(request.body)

        product = get_object_or_404(Product, slug=slug_field)
        quantity_in_cart = int(post_data["cart"].get(slug_field, 0))

        is_valid_quantity = utils.verify_quantity_in_cart(product, quantity_in_cart)
        if not is_valid_quantity:
            return JsonResponse({"error": "Quantity is invalid"}, safe=False)

        action = post_data["cart"].get("action", "")


        orderItem, created = OrderItems.objects.get_or_create(order=order, product=product)

        product_name = utils.get_plural_string(quantity_in_cart, product)
        orderItem.quantity += quantity_in_cart
        verify_quantity = utils.check_order_item(orderItem.quantity, product.max_quantity)

        try:
            if action == "add":
                if not verify_quantity:
                    product_plural_name = utils.create_plural_string(product.name)
                    return JsonResponse({"error":
                                        f"Cannot add any more"
                                        f" {product_plural_name } to your cart"
                                        f" {product.max_quantity }"
                                        f" is the maximum per order"}, safe=False)
                orderItem.save()
                return JsonResponse({"success": f"{quantity_in_cart} {product_name}"
                                    f" added to the cart"}, safe=False)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, safe=False)

