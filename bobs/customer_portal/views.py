from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class CustomerPortalDefaultView(LoginRequiredMixin, View):

    def get(self, request):
        customer = request.user.customer
        context = {"customer": customer}
        return render(request, "customer_portal/customer_portal.html", context)
