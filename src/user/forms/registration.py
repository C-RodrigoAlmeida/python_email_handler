from django import forms
from src.user.models.custom_user import CustomUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['employee_id', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'employee_id': forms.TextInput(attrs={'style': 'text-transform:uppercase;'}),
            'password': forms.PasswordInput()
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control backdrop-blur bg-[#202c33] mb-8 border-b-2 border-gray-300 w-full',
            })