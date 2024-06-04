"""Views to handle errors"""


from django.contrib.sitemaps import Sitemap
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET
from products.models import Product

robots_txt_file_content = """\
User-agent: *
Disallow: /admin*
Disallow: /customer*
Disallow: /admin/
Disallow: /cart/
Disallow: /checkout/
Disallow: /profile/
Disallow: /orders/
Disallow: /admin-portal/
Disallow: /admin-orders/
Disallow: /customer-portal/
Sitemap: sd-ci-pp5-bobs-and-babs-5fa3ca5e7225.herokuapp.com/sitemap.xml
"""


@require_GET
def robots_txt_file(request):
    return HttpResponse(robots_txt_file_content, content_type="text/plain")


@require_GET
def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "404.html", status=404)


@require_GET
def handler500(request):
    """ Error Handler 500 - Internal Server Error """
    return render(request, "500.html", status=500)


@require_GET
def handler403(request, exception):
    """ Error Handler 403 - Access denied """
    return render(request, "403.html", status=403)


class ShopSiteMap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Product.objects.filter(showing_in_shop=True)

    def lastmod(self, obj):
        return obj.last_modified
