from django.urls import path
from . import views

urlpatterns = [
    path('', views.GeneralPageDefaultView.as_view(), name='general_page_default_view'),
]