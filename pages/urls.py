from django.urls import path
from . views import Home_page,Contact_us,About_us

urlpatterns = [
    path('', view= Home_page.as_view(), name="index"),
    path('about_us/', view=About_us.as_view(), name="about"),
    path('contact_us/',view=Contact_us.as_view(), name="contact")
]
