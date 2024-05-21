import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order


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