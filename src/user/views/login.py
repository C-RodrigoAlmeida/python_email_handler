from django.contrib.auth.views import LoginView
from src.user.forms.login import LoginForm

class LoginView(LoginView):
    template_name = "login.html"
    form_class = LoginForm