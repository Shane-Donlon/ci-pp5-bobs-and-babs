from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_GET
from django_tables2 import RequestConfig
from products.models import Order, OrderItems

from .tables import orderTable


@method_decorator([require_GET, login_required], name='dispatch')
class GetAllOrdersView(View):
    def get(self, request):
        customer = request.user.customer
        orders = Order.objects.filter(customer=customer).order_by('-date_ordered')
        table = orderTable(
                orders,
                template_name="django_tables2/bootstrap5-responsive.html")
        RequestConfig(request).configure(table)
        table.paginate(page=request.GET.get("page", 1), per_page=10)

        context = {
            'table': table

        }
        return render(request, "customer_orders/customer_orders.html", context)


@method_decorator([require_GET, login_required], name='dispatch')
class GetSingularOrder(View):
    def get(self, request, transaction_id):
        order = get_object_or_404(Order, transaction_id=transaction_id)
        items = order.orderitems_set.all()

        if not request.user.customer:
            raise PermissionDenied

        if request.user.customer != order.customer:
            raise PermissionDenied

        for item in items:
            item.total_price = item.product.price * item.quantity

        context = {
                'order': order,
                'items': items
            }
        return render(request, "customer_orders/order.html", context)