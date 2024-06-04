from django.contrib import admin
from django.urls import include, path
from django.views.static import serve

from .views import handler403, handler404, handler500, robots_txt_file

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path("products/", include("products.urls")),
    path("accounts/", include("allauth.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("cart/", include("cart.urls")),
    path("checkout/", include("checkout.urls")),
    path("customer-portal/", include("customer_portal.urls")),
    path("profile/", include("customer_profile.urls")),
    path("orders/", include("customer_orders.urls")),
    path("admin-portal/", include("admin_portal.urls")),
    path("admin-orders/", include("admin_orders.urls")),
    path("robots.txt", robots_txt_file),
]

handler404 = 'bobs.views.handler404'
handler500 = 'bobs.views.handler500'
handler403 = 'bobs.views.handler403'
