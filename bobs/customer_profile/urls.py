from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProfilePageView.as_view(), name='profile'),
    path('update/', views.UpdateProfile.as_view(), name='update'),
]
