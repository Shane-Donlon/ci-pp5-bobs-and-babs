from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import (HttpResponsePermanentRedirect, get_object_or_404,
                              render)
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django_tables2 import RequestConfig
from products.models import Order, ShippingInformation

from .forms import AdminOrderUpdateForm
from .tables import OrderTableAdmin


def is_superuser(user):
    return user.is_superuser


@method_decorator(user_passes_test(is_superuser), name='dispatch')
class AdminOrdersAllOrders(View):

    def get(self, request, ):

        orders = Order.objects.all().order_by('-complete')

        table = OrderTableAdmin(
                orders,
                template_name="django_tables2/bootstrap5-responsive.html")
        RequestConfig(request).configure(table)
        table.paginate(page=request.GET.get("page", 1), per_page=10)

        context = {
            'table': table

        }
        if 'order_fulfilled' in request.session:

            context["success"] = request.session['order_fulfilled']
            del request.session['order_fulfilled']

        return render(request, "admin_orders/admin_orders.html", context)


@method_decorator(user_passes_test(is_superuser), name='dispatch')
class AdminOrdersIndividualOrder(View):
    def get(self, request, pk):

        order = get_object_or_404(Order, id=pk)
        items = order.orderitems_set.all()
        form = AdminOrderUpdateForm(instance=order)
        context = {
            'order': order,
            'items': items,
            'form': form
        }
        if order.delivery:
            shipping_information = ShippingInformation.objects.get(
                order=order.id)
            context["shipping_information"] = shipping_information

        return render(request, "admin_orders/individual_order/order.html",
                      context)

    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        order.fulfilled = True
        order.save()
        request.session["order_fulfilled"] = "Order Fulfilled successfully"
        redirect_url = reverse('admin_orders_view_all')
        return HttpResponsePermanentRedirect(redirect_url)
