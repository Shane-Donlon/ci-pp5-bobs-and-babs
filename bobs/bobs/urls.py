from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path("products", include("products.urls")),
    path("accounts/", include("allauth.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
