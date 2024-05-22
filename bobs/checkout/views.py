from django.shortcuts import redirect, render
from django.views import View
from products.models import Order, OrderItems, Product


class CheckoutPage(View):

    def get(self, request):
        if(request.user.is_authenticated):
            customer = request.user.customer
            try:
                order = Order.objects.get(customer=customer, complete=False)

            except Order.DoesNotExist:
                return redirect('cart')

            items = order.orderitems_set.all()
            if not items:
                return redirect('cart')
            context = {"items": items, "order": order, "customer":customer, 'is_checkout_page': True,}
            return render(request, "checkout/checkout.html", context)

        if request.session.get("customer"):
            try:
                order = Order.objects.get(transaction_id=request.session["customer"], complete=False)
            except Order.DoesNotExist:
                return redirect('cart')
            items = order.orderitems_set.all()
            if not items:
                return redirect('cart')
            context = {"items": items, "order": order, 'is_checkout_page': True,}
            return render(request, "checkout/checkout.html", context)
        else:
            # ie if the user does not have session data
            return redirect('cart')

