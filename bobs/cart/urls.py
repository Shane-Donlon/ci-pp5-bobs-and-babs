from django.urls import path

from . import views

urlpatterns = [
    path("", views.CartPageDefaultView.as_view(), name="cart"),
]
