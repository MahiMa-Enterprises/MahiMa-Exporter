from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, "website/home.html")


def about(request):
    return render(request, "website/about.html")


def products(request):
    return render(request, "website/products.html")


def affiliation(request):
    return render(request, "website/affiliation.html")


# =========================================================
# SEND ENQUIRY
# =========================================================

def enquiry(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name", "").strip()
        company_name = request.POST.get("company_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        country = request.POST.get("country", "").strip()
        product = request.POST.get("product", "").strip()
        quantity = request.POST.get("quantity", "").strip()
        packaging = request.POST.get("packaging", "").strip()
        message = request.POST.get("message", "").strip()

        subject = f"New Product Enquiry - {product or 'MahiMa Enterprises'}"

        email_body = f"""
NEW PRODUCT ENQUIRY
===================

CUSTOMER DETAILS
----------------

Full Name:
{full_name}

Company Name:
{company_name or "Not provided"}

Business Email:
{email}

Phone / WhatsApp:
{phone or "Not provided"}

Destination Country:
{country or "Not provided"}


REQUIREMENT
-----------

Product Required:
{product or "Not provided"}

Required Quantity:
{quantity or "Not provided"}

Packaging Requirement:
{packaging or "Not provided"}


MESSAGE / PRODUCT SPECIFICATION
--------------------------------

{message or "Not provided"}


===================

This enquiry was submitted through the
MahiMa Enterprises website.
"""

        try:

            send_mail(
                subject=subject,
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            return render(
                request,
                "website/enquiry.html",
                {
                    "success_message":
                        "Thank you. Your enquiry has been submitted successfully. "
                        "Our team will contact you soon."
                }
            )

        except Exception as e:

            print("========================================")
            print("ENQUIRY EMAIL ERROR:", repr(e))
            print("========================================")

            return render(
                request,
                "website/enquiry.html",
                {
                    "error_message":
                        f"EMAIL ERROR: {str(e)}"
                }
            )

    return render(request, "website/enquiry.html")


# =========================================================
# CONTACT US
# =========================================================

def contact(request):

    if request.method == "POST":

        # These names match the Contact Us HTML form
        full_name = request.POST.get("full_name", "").strip()
        company_name = request.POST.get("company_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        country = request.POST.get("country", "").strip()
        contact_subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        subject = (
            f"New Contact Message - "
            f"{contact_subject or 'MahiMa Enterprises'}"
        )

        email_body = f"""
NEW CONTACT MESSAGE
===================

CONTACT DETAILS
---------------

Full Name:
{full_name or "Not provided"}

Company Name:
{company_name or "Not provided"}

Business Email:
{email or "Not provided"}

Phone / WhatsApp:
{phone or "Not provided"}

Country:
{country or "Not provided"}


SUBJECT
-------

{contact_subject or "Not provided"}


MESSAGE / PRODUCT REQUIREMENT
------------------------------

{message or "Not provided"}


===================

This message was submitted through the
MahiMa Enterprises Contact Us page.
"""

        try:

            send_mail(
                subject=subject,
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            return render(
                request,
                "website/contact.html",
                {
                    "success_message":
                        "Thank you for contacting MahiMa Enterprises. "
                        "Your message has been sent successfully."
                }
            )

        except Exception as e:

            print("========================================")
            print("CONTACT EMAIL ERROR:", repr(e))
            print("========================================")

            return render(
                request,
                "website/contact.html",
                {
                    "error_message":
                        f"EMAIL ERROR: {str(e)}"
                }
            )

    return render(request, "website/contact.html")