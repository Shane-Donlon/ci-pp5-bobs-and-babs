from django.shortcuts import render
from django.views import View
class GeneralPageDefaultView(View):

    def get(self, request):
        return render(request, "customer_orders/customer_orders.html",)