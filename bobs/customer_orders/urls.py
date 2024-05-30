from django.urls import path

from . import views

urlpatterns = [
    path('', views.GetAllOrdersView.as_view(), name='orders'),
    path('view/<str:transaction_id>/', views.GetSingularOrder.as_view(), name='individual_order'),
]