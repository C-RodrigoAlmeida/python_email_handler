from django.forms import ModelForm
from src.inbox.models.recipient import Recipient

class RecipientRegistrationForm(ModelForm):
    class Meta:
        model = Recipient
        fields = ['name', 'last_name', 'email', 'employee_id']

    def __init__(self, *args, **kwargs):
        super(RecipientRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control backdrop-blur bg-gray-300/75 mb-8 border-b-2 border-green-900',
            })
