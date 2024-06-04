from django_tables2 import LinkColumn, TemplateColumn, tables
from django_tables2.utils import A
from products.models import Order


class orderTable(tables.Table):
    transaction_id = LinkColumn('individual_order',
                                text=lambda record: record.transaction_id,
                                args=[A('transaction_id')], attrs={
                                    "a": {"style": "color: #0055f2;",
                                          "aria-label": "open order"}})

    date_ordered = TemplateColumn(
        template_code="{{ record.date_ordered|date:'d/M/Y' }}"
    )
    delivery_fee = TemplateColumn(
        template_code="€{{ record.delivery_fee | floatformat:2 }}"
    )
    cart_total = TemplateColumn(
        template_code="€{{ record.cart_total | floatformat:2 }}"
    )

    class Meta:
        model = Order
        exclude = ('id', 'customer',)
