from django.views.generic import FormView
from src.user.forms.login import LoginForm

class LoginView(FormView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LoginForm