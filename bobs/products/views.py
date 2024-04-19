from django.shortcuts import render
from django.views import View

# Create your views here.


class ProductsPageDefaultView(View):

    def get(self, request):
        return render(request, "products/products.html", )
