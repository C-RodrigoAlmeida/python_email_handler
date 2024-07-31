from django.views.generic import CreateView
from src.user.models.custom_user import CustomUser
from src.user.forms.registration import RegistrationForm
from django.urls import reverse_lazy

class RegistrationView(CreateView):
    model = CustomUser
    form_class = RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy('user:login')