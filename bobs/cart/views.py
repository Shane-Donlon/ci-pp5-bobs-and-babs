import json

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from products.models import Order, OrderItems, Product

from . import utils


class CartPageDefaultView(View):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
        elif request.session.get("customer"):
            order = Order.objects.get(transaction_id=request.session.get("customer"))
            if order.complete:
                request.session.cycle_key()
                return render(request, "cart/cart.html", {})

        else:
            return render(request, "cart/cart.html", {})

        items = order.orderitems_set.all()
        context = utils.build_context(items, order)

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            # if request is from JavaScript
            context = utils.build_json_context(items, order)
            return JsonResponse(context, safe=False)

        return render(request, "cart/cart.html", context)


class updateCart(View):
    def post(self, request, slug_field):
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            post_data = json.loads(request.body)
            action = post_data["cart"]["action"]

            if action == "remove":
                product = Product.objects.get(slug=slug_field)
                order_number = post_data["cart"]["transactionId"]
                order = Order.objects.get(transaction_id=order_number)
                try:
                    order_item = OrderItems.objects.get(order=order, product=product)
                    order_item.delete()
                    order.save()
                    return JsonResponse({"success": f"{product.name} has been removed"})
                except ObjectDoesNotExist:
                    return JsonResponse({"error": "Item does not exist"})
                except IntegrityError:
                    return JsonResponse({"error": "An error occurred while trying to remove the item"})
