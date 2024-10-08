from django import forms
from src.inbox.models.recipient import Recipient

class RecipientBaseForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['employee_id', 'name', 'last_name', 'email']
        widgets = {
            'employee_id': forms.TextInput(attrs={'style': 'text-transform:uppercase;'}),
            'password': forms.PasswordInput()
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control backdrop-blur bg-[#202c33] mb-8 border-b-2 border-gray-300 w-full focus:outline-none focus:border-teal-800',
            })