from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdminPageDefault.as_view(), name='admin_portal'),
    path('<str:category>/add', views.AdminPageAdd.as_view(), name='admin_portal_add'),
    path('<str:category>/add/admin-post', views.AdminAddPostRequest.as_view(), name='admin_portal_add_admin_post'),
]