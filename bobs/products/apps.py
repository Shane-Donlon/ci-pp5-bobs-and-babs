from django.apps import AppConfig
from django.db.models.signals import post_save


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
    def ready(self):
        import products.signals
        post_save.connect(products.signals.update_cart_total, sender='products.Order')