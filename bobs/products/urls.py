from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductsPageDefaultView.as_view(), name="products"),
    path("<slug:slug_field>", views.ProductDetailView.as_view(), name="product-detail"),
    path("<slug:slug_field>/cart/add", views.AddToCart.as_view(), name="add-to-cart"),
    path("<slug:slug_field>/cart/remove", views.RemoveFromCart.as_view(), name="remove-from-cart"),
]