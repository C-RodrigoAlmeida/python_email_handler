from django.contrib.auth.models import User
from django.forms import ModelForm

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['employee_id', 'password']