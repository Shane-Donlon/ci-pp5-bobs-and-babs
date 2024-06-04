from django.urls import path

from . import views

urlpatterns = [
    path('', views.CustomerPortalDefaultView.as_view(),
         name='customer-portal'),

]
