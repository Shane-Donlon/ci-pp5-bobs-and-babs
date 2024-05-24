import json

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_GET, require_POST
from products.models import Order, OrderItems, Product

stripe.api_key = settings.STRIPE_SECRET_KEY


class CheckoutPage(View):

    def get(self, request):

        if (request.user.is_authenticated):
            customer = request.user.customer
            try:
                order = Order.objects.get(customer=customer, complete=False)

            except Order.DoesNotExist:
                return redirect('cart')

            items = order.orderitems_set.all()
            if not items:
                return redirect('cart')
            context = {"items": items, "order": order,
                       "customer": customer, 'is_checkout_page': True, }
            return render(request, "checkout/checkout.html", context)

        if request.session.get("customer"):
            try:
                order = Order.objects.get(
                    transaction_id=request.session["customer"], complete=False)
            except Order.DoesNotExist:
                return redirect('cart')
            items = order.orderitems_set.all()
            if not items:
                return redirect('cart')
            context = {"items": items, "order": order,
                       'is_checkout_page': True, }
            return render(request, "checkout/checkout.html", context)
        else:
            # ie if the user does not have session data
            return redirect('cart')





@method_decorator(require_POST, name='dispatch')
class Charge(View):
    def post(self, request, transaction_id):
        post_data = json.loads(request.body)

        stripe_token = post_data["stripeToken"]
        order = get_object_or_404(Order, transaction_id=transaction_id)
        delivery_selected = post_data["delivery"]
        if delivery_selected:
            order.delivery = True
            order.save()

        total_data = order.get_cart_total()
        total = int(float(total_data) * 100)
        customer_full_name = post_data["full-name"]
        email_address = post_data["email"]
        cost_data = post_data["cost"]
        cost = int(float(cost_data) * 100)


        if cost == total:
            try:
                customer_for_stripe = stripe.Customer.create(
                    name=customer_full_name,
                    email=email_address,
                    source=stripe_token,
                    description=transaction_id
                )

                charge = stripe.Charge.create(
                    amount=total,
                    currency="eur",
                    description=f"Payment for order{order.transaction_id}",
                    customer=customer_for_stripe,
                )

                if charge.paid:

                    order.complete = True
                    order.save()
                    invoice_item = stripe.InvoiceItem.create(
                        customer=customer_for_stripe.id,
                        amount=total,
                        currency="eur",
                        description=f"Payment for order{order.transaction_id}",)

                    invoice = stripe.Invoice.create(
                        customer=customer_for_stripe.id,
                        auto_advance=True  # Auto-finalize this draft after ~1 hour
                    )
                    invoice.finalize_invoice()

                    request.session["invoice_url"] = invoice.hosted_invoice_url
                    print(request.session["invoice_url"])
                    return JsonResponse({'redirect_url': reverse('order_complete')})

            except stripe.error.InvalidRequestError as e:
                return JsonResponse({"error": f"{e}"}, safe=False)
            except stripe.error.CardError as e:
                JsonResponse({"error": f"{e}"}, safe=False)
        if cost != total:
            return JsonResponse({"error": "An error has occurred <br/> "
                                 "Please contact us by phone to complete the order"}, safe=False)
        return JsonResponse({"error": "Payment failed"}, safe=False)


