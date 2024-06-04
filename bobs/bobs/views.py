"""Views to handle errors"""
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

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