from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from website.sitemaps import StaticViewSitemap


sitemaps = {
    "static": StaticViewSitemap,
}


def sitemap_view(request):
    response = sitemap(
        request,
        sitemaps=sitemaps,
    )

    response.headers.pop("X-Robots-Tag", None)

    return response


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "sitemap.xml",
        sitemap_view,
        name="sitemap",
    ),

    path("", include("website.urls")),
]