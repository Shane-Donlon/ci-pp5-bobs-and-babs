import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from products.models import Customer

from . import forms


class ProfilePageView(View):

    def get(self, request):

        customer = get_object_or_404(Customer, user=request.user.customer.user_id)
        form = forms.ProfileForm(instance=customer, initial={"user": request.user.customer})
        context = {"form": form}
        return render(request, "customer_profile/customer_profile.html",context)

    def post(self, request):
        post_data = json.loads(request.body)
        form = forms.ProfileForm(post_data)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": "Profile updated successfully"})

        return JsonResponse({"error": form.errors})
