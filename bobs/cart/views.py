import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from products.models import Order, OrderItems, Product

# Create your views here.


class CartPageDefaultView(View):
    def get(self, request):
        if(request.user.is_authenticated):
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitems_set.all()
            context = {"items": items, "order": order, "created": created,}

            if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                # if request is from JavaScript
                items_json = serializers.serialize('json', items)
                context = {"items": items_json, "order": serializers.serialize('json', [order]), "created": created,}
                return JsonResponse(context, safe=False)
            return render(request, "cart/cart.html", context)

        if request.session.get("customer"):
            print("get request here")
            order = Order.objects.get(transaction_id=request.session.get("customer"))
            if order.complete:
                request.session.cycle_key()
                return render(request, "cart/cart.html", {})

            items = order.orderitems_set.all()
            context = {"items": items, "order": order }
            if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                items_json = serializers.serialize('json', items)
                context = {"items": items_json, "order": serializers.serialize('json', [order]), }
                return JsonResponse(context, safe=False)
            return render(request, "cart/cart.html", context)
        else:
            return render(request, "cart/cart.html", {})


class updateCart(View):

    def post(self, request, slug_field):
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            post_data = json.loads(request.body)
            action = post_data["cart"]["action"]

            if action == "remove":
                product = Product.objects.get(slug=slug_field)
                order_number = post_data["cart"]["transactionId"]
                order = Order.objects.get(transaction_id=order_number)
                order_item = OrderItems.objects.get(order=order, product=product)
                try:
                    order_item.delete()
                    order.save()
                    return JsonResponse({"success": f"{product.name} has been removed"})
                except:
                    return JsonResponse({"error": "An error occurred, item has not been removed"})

