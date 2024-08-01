from django.views.generic import CreateView
from src.user.models.custom_user import CustomUser
from src.user.forms.registration import RegistrationForm
from django.urls import reverse_lazy

class RegistrationView(CreateView):
    model = CustomUser
    form_class = RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = user.employee_id 
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)
