from src.user.models.custom_user import CustomUser
from django.forms import ModelForm

class LoginForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['employee_id', 'password']