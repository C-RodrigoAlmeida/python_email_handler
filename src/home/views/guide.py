from django.views.generic import TemplateView

class Guide(TemplateView):
    template_name = 'guide.html'