from django.views.generic import TemplateView

class About_us(TemplateView):
    template_name = "pages/about_us.html"

class Home_page(TemplateView):
    template_name="pages/home.html"

class Contact_us(TemplateView):
    template_name="pages/contact_us.html"