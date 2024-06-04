from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdminOrdersAllOrders.as_view(),
         name='admin_orders_view_all'),
    path('<int:pk>/', views.AdminOrdersIndividualOrder.as_view(),
         name='admin_orders_view_individual'),
]
