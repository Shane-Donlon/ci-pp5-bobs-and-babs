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


