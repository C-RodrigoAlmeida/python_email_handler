from django.forms import ModelForm
from django.contrib.auth.models import User
from src.email_storage.models.recipient import Recipient

class RecipientRegistrationForm(ModelForm):
    class Meta:
        model = Recipient
        fields = ['name', 'last_name', 'email', 'employee_id']