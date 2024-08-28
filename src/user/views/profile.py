from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileView(TemplateView, LoginRequiredMixin):
    template_name = "profile.html"