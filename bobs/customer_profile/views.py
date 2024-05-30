import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from . import forms


class ProfilePageView(View):

    def get(self, request):
        initial_data = {
    'user': request.user.customer.user.username,
    'first_name': request.user.customer.first_name,
    'last_name': request.user.customer.last_name,
    'email': request.user.customer.email,
    'address': request.user.customer.address,
    'town': request.user.customer.town,
    'county': request.user.customer.county,
    'eircode': request.user.customer.eircode,
    'phone': request.user.customer.phone,
}
        form = forms.ProfileForm(initial=initial_data)
        context = {"form": form}
        print(request.user.customer)
        return render(request, "customer_profile/customer_profile.html",context)
