from django.views.generic import TemplateView
from src.user.models.custom_user import CustomUser
from src.user.forms.registration import RegistrationForm

class RegistrationView(TemplateView):
    template_name = "user/registration.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RegistrationForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create_user(
                employee_id=form.cleaned_data["employee_id"],
                name=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            user.save()
        return self.form_invalid(form) if user is None else self.form_valid(form, user)