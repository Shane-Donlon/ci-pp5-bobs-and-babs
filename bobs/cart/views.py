import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from products.models import Order

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


