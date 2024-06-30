from django.forms import ModelForm
from src.user.models.custom_user import CustomUser

class RegistrationForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['employee_id','name', 'email', 'password']