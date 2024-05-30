from django.urls import path

from . import views

urlpatterns = [
    path('', views.GeneralPageDefaultView.as_view(), name='orders'),
]