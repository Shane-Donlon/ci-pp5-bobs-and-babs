import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_GET, require_POST

from . import utils
from .models import Order, OrderItems, Product

# Create your views here.


@method_decorator(require_GET, name='dispatch')
class ProductsPageDefaultView(View):

    def get(self, request):
        products = Product.objects.filter(showing_in_shop=True)
        context = {
            "products": products
        }

        return render(request, "products/products.html", context)


@method_decorator(require_GET, name='dispatch')
class ProductDetailView(View,):
    def get(self, request, slug_field):
        product = get_object_or_404(Product, slug=slug_field)

        context = {
            "product": product,


        }
        return render(request, "products/product.html", context)


@method_decorator(require_POST, name='dispatch')
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
                order = Order.objects.get(
                    transaction_id=request.session.get("customer"))
                if order.complete:
                    order = utils.un_authenticated_order_complete(request)

        post_data = json.loads(request.body)

        product = get_object_or_404(Product, slug=slug_field)
        quantity_in_cart = int(post_data["cart"].get(slug_field, 0))

        is_valid_quantity = utils.verify_quantity_in_cart(
            product, quantity_in_cart)
        if not is_valid_quantity:
            return JsonResponse({"error": "Quantity is invalid"}, safe=False)

        action = post_data["cart"].get("action", "")

        orderItem, created = OrderItems.objects.get_or_create(
                order=order, product=product)

        product_name = utils.get_plural_string(quantity_in_cart, product)
        orderItem.quantity += quantity_in_cart
        verify_quantity = utils.check_order_item(
                                        orderItem.quantity,
                                        product.max_quantity)

        try:
            if action == "add":
                if not verify_quantity:
                    product_plural_name = utils.create_plural_string(
                        product.name)
                    return JsonResponse({"error":
                                        f"Cannot add any more"
                                         f" {product_plural_name} to your cart"
                                         f" {product.max_quantity }"
                                         f" is the maximum per order"},
                                        safe=False)
                orderItem.save()
                return JsonResponse({"success": f"{quantity_in_cart} "
                                     f"{product_name}"
                                    f" added to the cart"}, safe=False)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, safe=False)


@method_decorator(require_POST, name='dispatch')
class RemoveFromCart(View):

    def post(self, request, slug_field):
        post_data = json.loads(request.body)
        transaction_id = post_data["cart"]["transactionId"]
        if transaction_id:
            order = Order.objects.get(transaction_id=transaction_id)
            order_item = OrderItems.objects.get(order=order,
                                                product__slug=slug_field)

            product_name = utils.create_plural_string(order_item.product.name)

            try:
                order_item.delete()
                order.save()
                return JsonResponse({"success": f"{product_name} "
                                    "removed from cart"})
            except ObjectDoesNotExist:
                return JsonResponse({"error": "Item does not exist"})
            except Exception as e:
                return JsonResponse({"error": "An error occurred: " + str(e)})
        return JsonResponse({"error": "An error occurred"})
