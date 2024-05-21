from django.shortcuts import render
from django.views import View
from products.models import Order, OrderItems, Product


class CheckoutPage(View):

    def get(self, request):
        if(request.user.is_authenticated):
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitems_set.all()
            context = {"items": items, "order": order, "created": created,"customer":customer, }
            return render(request, "checkout/checkout.html", context)


            # session key is used to identify the order transaction
            # only created on post request of product detail view
        if request.session.get("customer"):
            order = Order.objects.get(transaction_id=request.session["customer"])
            items = order.orderitems_set.all()
            context = {"items": items, "order": order, }
            return render(request, "checkout/checkout.html", context)
        else:
            return render(request, "checkout/checkout.html")

