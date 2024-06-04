from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdminPageDefault.as_view(), name='admin_portal'),
    path('<str:category>/add', views.AdminPageAdd.as_view(), name='admin_portal_add'),
    path('<str:category>/add/admin-post', views.AdminAddPostRequest.as_view(), name='admin_portal_add_admin_post'),
    path('<str:category>/update', views.AdminPageEdit.as_view(), name='admin_portal_update'),
    path('products/update/<int:pk>', views.AdminPageEditIndividual.as_view(), name='products_update_pk'),
    path('products/delete', views.AdminPageDeleteProducts.as_view(), name='admin_portal_delete_products'),
    path('products/delete/<int:pk>', views.AdminPageDeleteIndividualProduct.as_view(), name='products_delete_pk'),

]