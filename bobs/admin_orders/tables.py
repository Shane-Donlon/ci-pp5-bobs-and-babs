from django.utils.html import format_html
from django_tables2 import Column, LinkColumn, TemplateColumn, tables
from django_tables2.utils import A
from products.models import Order


class SelectColumn(Column):
    def render(self, record):
        display_value = "Yes" if record.fulfilled else "No"
        return format_html(
            '<select name="fulfilled" data-order-id="{}">'
            '<option value="{}" selected>{}</option>'

            '</select>',
            record.id,
            record.fulfilled, display_value,
            not record.fulfilled, "No" if display_value == "Yes" else "Yes"
        )


class OrderTableAdmin(tables.Table):
    id = LinkColumn('admin_orders_view_individual',
                    text=lambda record: record.id,
                    args=[A('id')], attrs={
                               "a": {"style": "color: #0055f2;",
                                     "aria-label": "open product"}})
    fulfilled = SelectColumn()

    class Meta:
        model = Order
        fields = ["id", "customer", "complete", "date_ordered",
                  "transaction_id", "fulfilled"]
