from django.urls import path
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

]