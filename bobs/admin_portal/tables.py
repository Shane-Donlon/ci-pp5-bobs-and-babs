from django_tables2 import LinkColumn, tables
from django_tables2.utils import A
from products.models import Product


class ProductTable(tables.Table):
    id = LinkColumn('products_update_pk',
                           text=lambda record: record.id,
                           args=[A('id')], attrs={
                               "a": {"style": "color: #0055f2;",
                                     "aria-label": "open product"}})

    class Meta:
        model = Product
        exclude = [ 'image', 'description', 'price', 'category', 'allergin_info', "slug","Image description","sku"]

class ProductTableDelete(tables.Table):
    id = LinkColumn('products_delete_pk',
                           text=lambda record: record.id,
                           args=[A('id')], attrs={
                               "a": {"style": "color: #0055f2;",
                                     "aria-label": "open product"}})

    class Meta:
        model = Product
        exclude = [ 'image', 'description', 'price', 'category', 'allergin_info', "slug","Image description","sku"]