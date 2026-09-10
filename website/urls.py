from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "about/",
        views.about,
        name="about"
    ),

    path(
        "products/",
        views.products,
        name="products"
    ),

    path(
        "affiliation/",
        views.affiliation,
        name="affiliation"
    ),

    path(
        "enquiry/",
        views.enquiry,
        name="enquiry"
    ),

    path(
        "contact/",
        views.contact,
        name="contact"
    ),

    # Google Search Console verification
    path(
        "googlef24fe2e733aa6bfa.html",
        views.google_verification,
        name="google_verification"
    ),

    # Robots.txt
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain"
        ),
        name="robots_txt"
    ),

]