from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import Product

# Create your views here.


class ProductsPageDefaultView(View):

    def get(self, request):
        products = Product.objects.all()
        context = {
            "products": products
        }

        return render(request, "products/products.html",context )


class ProductDetailView(View,):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        allergens = product.allergin_info.split('\n')
        contains = allergens[0].split(":")[1].split(",")
        may_contain = allergens[1].split(":")[1].split(",")

        context = {
            "product": product,
            "contains": contains,
            "may_contain": may_contain,
        }

        return render(request, "products/product.html", context)