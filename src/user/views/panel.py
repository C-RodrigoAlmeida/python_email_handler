from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class PanelView(TemplateView, LoginRequiredMixin):
    template_name = 'panel.html'