from django.urls import path

from . import views

urlpatterns = [
    path("", views.CartPageDefaultView.as_view(), name="cart"),
    path("update/<slug:slug_field>/", views.updateCart.as_view(), name="update_cart"),
]
