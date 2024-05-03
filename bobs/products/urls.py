from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductsPageDefaultView.as_view(), name="products"),
]
