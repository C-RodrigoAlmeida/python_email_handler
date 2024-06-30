from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from src.user.forms.login import LoginForm


class LoginView(TemplateView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LoginForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
        
        return self.form_invalid(form) if user is None else self.form_valid(form, user)

