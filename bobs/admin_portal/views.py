
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django_tables2 import RequestConfig
from products.models import Product

from .forms import AddProductForm
from .tables import ProductTable, ProductTableDelete


def is_superuser(user):
    return user.is_superuser


@method_decorator(user_passes_test(is_superuser), name='dispatch')
class AdminPageDefault(View):

    def get(self, request):
        if 'deleted_product' in request.session:
            # if redirected from delete request on products delete
            # see AdminPageDeleteIndividualProduct view
            del request.session['deleted_product']
            context = {"success": "Product deleted successfully"}
            return render(request, "admin_portal/admin_portal.html", context)
        if 'added_product' in request.session:
            # if redirected from add request on products add
            # see AdminAddPostRequest view
            context = {"success": request.session['added_product']}
            del request.session['added_product']
            return render(request, "admin_portal/admin_portal.html", context)
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

            if Product.objects.filter(name=request.POST['name']).exists():
                return JsonResponse({"error":
                                    "A product with this name already exists"})

            if product_form.is_valid():
                product_form.save()
                name = product_form.cleaned_data['name']
                message = f'Product {name} Added successfully'
                request.session['added_product'] = message

                redirect_url = reverse('admin_portal')
                return JsonResponse({'redirect': redirect_url})
            else:
                return JsonResponse({"error": product_form.errors})

        return render(request, "admin_portal/add/add.html")


@method_decorator(user_passes_test(is_superuser), name='dispatch')
class AdminPageEdit(View):
    def get(self, request, category):
        if category == "product":
            products = Product.objects.all()
            table = ProductTable(
                products,
                template_name="django_tables2/bootstrap5-responsive.html")
            RequestConfig(request).configure(table)
            table.paginate(page=request.GET.get("page", 1), per_page=10)
            context = {"product_table": table}
            if request.session.get('updated_product'):
                # if redirected from update request on products update
                # see AdminPageEditIndividual view
                context = {"success": request.session['updated_product'],
                           "product_table": table}
                del request.session['updated_product']
            return render(request, "admin_portal/update/update.html", context)
        return render(request, "admin_portal/admin_portal.html")


@method_decorator(user_passes_test(is_superuser), name='dispatch')
class AdminPageEditIndividual(View):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        product_form = AddProductForm(instance=product)
        context = {
            "product_form": product_form
        }
        return render(request, "admin_portal/update/update_individual.html",
                      context)

    def post(self, request, pk):

        product = Product.objects.get(pk=pk)
        product_form = AddProductForm(
            request.POST, request.FILES, instance=product)

        if product_form.is_valid():
            product_form.save()
            name = product.name
            message = f'Product {name} Updated successfully'
            request.session['updated_product'] = message
            redirect_url = reverse('admin_portal_update', args=["product"])
            return JsonResponse({'redirect': redirect_url})
        else:
            return JsonResponse({"error": product_form.errors})


@method_decorator(user_passes_test(is_superuser), name='dispatch')
class AdminPageDeleteProducts(View):

    def get(self, request, ):
        products = Product.objects.all()

        table = ProductTableDelete(
                products,
                template_name="django_tables2/bootstrap5-responsive.html")
        RequestConfig(request).configure(table)
        table.paginate(page=request.GET.get("page", 1), per_page=10)
        context = {"product_table": table}
        return render(request, "admin_portal/delete/delete.html", context)

    def post(self, request, pk):

        product = Product.objects.get(pk=pk)
        product_form = AddProductForm(
            request.POST, request.FILES, instance=product)

        if product_form.is_valid():
            product_form.save()
            return JsonResponse({"success": "Product updated successfully"})
        else:
            return JsonResponse({"error": product_form.errors})


@method_decorator(user_passes_test(is_superuser), name='dispatch')
class AdminPageDeleteIndividualProduct(View):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        product_form = AddProductForm(instance=product)
        context = {"product_form": product_form}

        return render(request, "admin_portal/delete/delete_individual.html",
                      context)

    def delete(self, request, pk):

        product = Product.objects.get(pk=pk)

        product.delete()
        request.session['deleted_product'] = 'Product deleted successfully'
        redirect_url = reverse('admin_portal')
        return JsonResponse({'redirect': redirect_url})
