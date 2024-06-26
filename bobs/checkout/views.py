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

from . import utils
from .forms import ShippingInformationFrom

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

            form = ShippingInformationFrom(initial={
                "first_name": customer.first_name,
                "last_name": customer.last_name,
                "email": customer.email,
                "phone": customer.phone,
                "address": customer.address,
                "town": customer.town,
                "county": customer.county,
                "eircode": customer.eircode
            })
            context = {"items": items, "order": order,
                       "customer": customer, 'is_checkout_page': True,
                                             "form": form}
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
            form = ShippingInformationFrom()
            context = {"items": items, "order": order,
                       'is_checkout_page': True,
                       "form": form}
            return render(request, "checkout/checkout.html", context)
        else:
            # ie if the user does not have session data
            return redirect('cart')


@method_decorator(require_POST, name='dispatch')
class CheckoutComplete(View):
    def post(self, request):
        order = Order.objects.get(
            transaction_id=request.session["customer"], complete=False)
        order.complete = True
        order.save()
        return redirect('order_complete')


@method_decorator(require_POST, name='dispatch')
class Charge(View):
    def post(self, request, transaction_id):
        # TODO refactor with 2 urls for post if order and if not order
        order = get_object_or_404(Order, transaction_id=transaction_id)
        data = json.loads(request.body)
        post_data = data["order"]

        stripe_token = post_data["stripeToken"]
        order = get_object_or_404(Order, transaction_id=transaction_id)
        delivery_selected = post_data["delivery"]
        # this is not behind an if statement
        # if wrapped in an if statement and the first post request fails
        # then the order will be out of sync and will never execute correctly

        order.delivery = delivery_selected
        delivery_form = None
        if post_data["delivery"]:
            try:
                email_data = data["email"]

                delivery_form = ShippingInformationFrom(email_data)
                if request.user.is_authenticated:
                    customer = request.user.customer
                    if delivery_form.is_valid():
                        delivery_info = delivery_form.save(commit=False)
                        delivery_info.customer = customer
                        delivery_info.order = order
                        delivery_info.save()
                    if not delivery_form.is_valid():
                        return JsonResponse({"error": "An error has occurred"
                                            "Form Invalid <br/> "
                                             "Please contact us by phone to"
                                             "complete the order"}, safe=False)

                if not request.user.is_authenticated:
                    if delivery_form.is_valid():
                        delivery_info = delivery_form.save(commit=False)
                        delivery_info.customer = None
                        delivery_info.order = order
                        delivery_info.save()
                    if not delivery_form.is_valid():
                        return JsonResponse({"error": "An error has "
                                             "Please contact us by phone to"
                                             "complete the order"}, safe=False)

            except ValueError as e:
                return JsonResponse({"error": f"{e}"}, safe=False)

        total_data = order.get_cart_total()
        total = int(float(total_data) * 100)
        customer_full_name = post_data["full-name"]
        email_address = post_data["email"]
        cost_data = post_data["cost"]
        cost = int(float(cost_data) * 100)

        if cost == total:
            try:
                customer_for_stripe = utils.create_stripe_customer(
                        customer_full_name, email_address, stripe_token,
                        transaction_id)
                charge = utils.create_stripe_charge(
                    customer_for_stripe, total, transaction_id)

                if charge.paid:
                    order.complete = True
                    if not order.delivery:
                        order.delivery_fee = 0
                    order.save()
                    if delivery_form:
                        delivery_form.save()
                    invoice = utils.create_stripe_invoice(
                            customer_for_stripe, total, transaction_id)
                    request.session["invoice_url"] = invoice.hosted_invoice_url
                    return JsonResponse({'redirect_url': reverse(
                        'order_complete')})

            except stripe.error.InvalidRequestError as e:
                return JsonResponse({"error": f"{e}"}, safe=False)
            except stripe.error.CardError as e:
                JsonResponse({"error": f"{e}"}, safe=False)
        if cost != total:
            return JsonResponse({"error": "An error has occurred cost<br/> "
                                "Please contact us by phone "
                                 "to complete the order"}, safe=False)
        return JsonResponse({"error": "Payment failed"}, safe=False)


@method_decorator(require_GET, name='dispatch')
class OrderSuccess(View):
    def get(self, request):
        if request.session.get("invoice_url"):
            invoice_url = request.session["invoice_url"]
            # pop method removes the key-value pair from the session
            # but does not raise error if not found
            request.session.pop("customer", None)
            request.session.pop("invoice_url", None)

            context = {"invoice_url": invoice_url}
            return render(request, "checkout/order/order_complete.html",
                          context)
        return redirect('index')
