from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductsPageDefaultView.as_view(), name="products"),
    path("<slug:slug_field>", views.ProductDetailView.as_view(), name="product_detail"),
]