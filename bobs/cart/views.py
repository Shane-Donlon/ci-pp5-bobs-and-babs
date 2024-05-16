from django.shortcuts import render
from django.views import View
from products.models import Order, OrderItems, Product

# Create your views here.


class CartPageDefaultView(View):

    def get(self, request):
        if(request.user.is_authenticated):
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitems_set.all()
            context = {"items": items, "order": order, "created": created,}
            return render(request, "cart/cart.html", context)

        else:
            items = []
            order = {"get_cart_total": 0, "get_cart_items": 0}
            context = {"max_quantity": 10, }
            return render(request, "cart/cart.html", context)
