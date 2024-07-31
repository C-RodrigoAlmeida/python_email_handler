from django.forms import ModelForm
from src.inbox.models.recipient import Recipient

class RecipientRegistrationForm(ModelForm):
    class Meta:
        model = Recipient
        fields = ['name', 'last_name', 'email', 'employee_id']