from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from src.user.forms.login import LoginForm

class LoginView(LoginView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy('user:panel')