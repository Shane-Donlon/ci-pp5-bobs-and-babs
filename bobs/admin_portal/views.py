from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from products.models import Product

from.forms import AddProductForm

def is_superuser(user):
    return user.is_superuser

@method_decorator(user_passes_test(is_superuser), name='dispatch')
class AdminPageDefault(View):

    def get(self, request):
        return render(request, "admin_portal/admin_portal.html")


@method_decorator(user_passes_test(is_superuser), name='dispatch')
class AdminPageAdd(View):

    def get(self, request, category):
        if category == "product":
            context = {
                "product_form": AddProductForm()
            }
            return render(request, "admin_portal/add/add.html", context)
        return render(request, "admin_portal/admin_portal.html")




@method_decorator(user_passes_test(is_superuser), name='dispatch')

class AdminAddPostRequest(View):
    def post(self, request, category):
        if category == "product":
            product_form = AddProductForm(request.POST, request.FILES)

            if not "contains:" in request.POST["allergin_info"]:
                return JsonResponse({"error": "Incorrect Format Example"
                                     "</br> contains: nuts, dairy, gluten,"
                                     "may contain: peanuts"})

            if not "may contain:" in request.POST["allergin_info"]:
                return JsonResponse({"error": "Incorrect Format Example"
                                     "</br> contains: nuts, dairy, gluten,"
                                     "may contain: peanuts"})

            if Product.objects.filter(name=request.POST['name']).exists():
                return JsonResponse({"error": "A product with this name already exists"})

            if product_form.is_valid():
                product_form.save()
                return JsonResponse({"success": "Product added successfully"})
            else:
                return JsonResponse({"error": product_form.errors})

        return render(request, "admin_portal/add/add.html")