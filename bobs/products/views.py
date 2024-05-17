import json

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


class addToCart(View):
    def get(self, request, slug_field):
        return JsonResponse({"success": True})


    def post(self, request, slug_field):
        cart = request.session.get("cart", {})
        post_data = json.loads(request.body)
        product = get_object_or_404(Product, slug=slug_field)
        quantity_in_cart = int(post_data["cart"].get(slug_field, 0))
        is_valid_quantity = utils.verify_quantity_in_cart(product, quantity_in_cart)
        if not is_valid_quantity:
            return JsonResponse({"error": "Quantity is invalid"}, safe=False)

        action = post_data["cart"].get("action", "")
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItems.objects.get_or_create(order=order, product=product)
        if action == "add":
            product_name = utils.get_plural_string(quantity_in_cart, product)
            orderItem.quantity += quantity_in_cart
            verify_quantity = utils.check_order_item(orderItem.quantity, product.max_quantity)
            if not verify_quantity:
                if product_name[-1] != "s":
                    product_name = f"{product_name}s"
                return JsonResponse({"error":
                                     f"Cannot add any more"
                                     f" {product_name } to your cart"
                                     f" {product.max_quantity }"
                                     f" is the maximum per order"}, safe=False)
            orderItem.save()
            return JsonResponse({"success": f"{quantity_in_cart} {product_name}"
                                 f" added to the cart"}, safe=False)
        if action == "remove":
            orderItem.delete()
            return JsonResponse({"success": True}, safe=False)

        return JsonResponse({"success": True}, safe=False)
