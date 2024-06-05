import uuid

from allauth.account.signals import user_signed_up
from django.contrib.auth.signals import user_logged_in
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Customer, Order


@receiver(post_save, sender=Order)
def update_cart_total(sender, instance, **kwargs):

    cart_total = instance.get_cart_total()
    if cart_total != instance.cart_total:
        instance.cart_total = cart_total
        instance.save(update_fields=['cart_total'])


@receiver(post_save, sender=Order)
def update_transaction_id(sender, instance, **kwargs):
    if not instance.transaction_id:
        instance.transaction_id = str(uuid.uuid4())
        instance.save(update_fields=['transaction_id'])


@receiver(user_signed_up)
def create_customer_profile(request, user, **kwargs):
    user.username = user.email
    user.save()
    customer = Customer.objects.create(user=user, email=user.email)
    customer.save()


@receiver(user_logged_in)
def user_signed_in(sender, user, request, **kwargs):
    if request.session.get("customer"):
        # if the user started as unauthenticated
        # then logged in migrate the order
        customer = user.customer
        order_exists = Order.objects.filter(
            transaction_id=request.session["customer"],
            complete=False).exists()
        order = None
        if order_exists:
            order = Order.objects.get(
                            transaction_id=request.session["customer"],
                            complete=False)

        customer_order_exists = Order.objects.filter(customer=customer,
                                                     complete=False).exists()
        if customer_order_exists and order_exists:
            customer_order = (
                             Order.objects.get(customer=customer,
                                               complete=False))
            for item in order.orderitems_set.all():
                existing_item = (
                    customer_order.orderitems_set
                    .filter(product=item.product)
                )
                if existing_item.exists():
                    # If the item exists, increment the quantity
                    existing_item.update(
                                        quantity=F('quantity') + item.quantity
                                        )

                    updated_item = existing_item.first()
                    updated_item.save()
                    if (
                     updated_item.quantity > updated_item.product.max_quantity
                    ):
                        updated_item.quantity = (
                            updated_item.product.max_quantity
                        )
                        updated_item.save()
                else:
                    item.order = customer_order
                    item.save()
            order.delete()
            request.session.pop("customer", None)
            return

        if not customer_order_exists and order_exists:
            order.customer = customer
            order.save()

        if order is None:
            return
