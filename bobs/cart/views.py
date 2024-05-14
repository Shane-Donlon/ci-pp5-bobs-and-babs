from django.shortcuts import render
from django.views import View

# Create your views here.


class CartPageDefaultView(View):

    def get(self, request):

        context = {"max_quantity": 10, }
        return render(request, "cart/cart.html", context)
