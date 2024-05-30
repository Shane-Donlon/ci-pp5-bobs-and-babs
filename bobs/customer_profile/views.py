import json

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_GET, require_POST
from products.models import Customer

from . import forms


@method_decorator([login_required,require_GET], name='dispatch')
class ProfilePageView(View):
    def get(self, request):
        customer = get_object_or_404(Customer, user=request.user.customer.user_id)
        form = forms.ProfileForm(instance=customer, initial={"user": request.user.customer})
        context = {"form": form}
        return render(request, "customer_profile/customer_profile.html",context)


@method_decorator([login_required, require_POST], name='dispatch')
class UpdateProfile(View):
    def post(self, request):
        try:
            customer = Customer.objects.get(id=request.user.customer.id)
            post_data = json.loads(request.body)
            form_data = post_data["order"]
            form_data["user"] = customer.pk
            form = forms.ProfileForm(form_data, instance=customer)

            if form.is_valid():
                form.save()
                return JsonResponse({"success": "Profile updated successfully"})
            else:
                return JsonResponse({"error": form.errors.as_text()}, status=400)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Customer not found"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
