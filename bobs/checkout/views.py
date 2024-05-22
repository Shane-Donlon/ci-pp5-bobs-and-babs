from django.shortcuts import render
from django.views import View
from products.models import Order, OrderItems, Product


class CheckoutPage(View):

    def get(self, request):
        if(request.user.is_authenticated):
            customer = request.user.customer
            try:
                order = Order.objects.get(customer=customer, complete=False)

            except Order.DoesNotExist:
                return render(request, "checkout/checkout.html", {})

            items = order.orderitems_set.all()
            context = {"items": items, "order": order, "created": created,"customer":customer, }
            return render(request, "checkout/checkout.html", context)

        if request.session.get("customer"):
            try:
                order = Order.objects.get(transaction_id=request.session["customer"], complete=False)
            except Order.DoesNotExist:
                return render(request, "checkout/checkout.html", {})
            items = order.orderitems_set.all()
            context = {"items": items, "order": order, }
            return render(request, "checkout/checkout.html", context)
        else:
            return render(request, "checkout/checkout.html")

