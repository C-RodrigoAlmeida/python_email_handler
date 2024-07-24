from django.views.generic import CreateView
from src.user.models.custom_user import CustomUser
from src.user.forms.registration import RegistrationForm

class RegistrationView(CreateView):
    model = CustomUser
    form_class = RegistrationForm
    template_name = "registration.html"
