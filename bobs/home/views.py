from django.shortcuts import render
from django.views import View

# Create your views here.


class IndexPageView(View):

    def get(self, request):
        return render(request, "home/home.html", )
