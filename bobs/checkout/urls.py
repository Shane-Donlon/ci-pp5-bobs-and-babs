from django.urls import path

from . import views

urlpatterns = [
    path('', views.CheckoutPage.as_view(), name='checkout'),
    path("charge/<str:transaction_id>/", views.Charge.as_view(), name="charge"),
    path("order-success/", views.OrderSuccess.as_view(), name="order_complete"),
]