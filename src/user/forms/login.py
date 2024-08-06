from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    fields = ['username', 'password']
    widgets = {
        'username': forms.TextInput(attrs={'style': 'text-transform:uppercase;'}),
        'password': forms.PasswordInput()
    }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Employee ID'
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control backdrop-blur bg-slate-300 mb-8 border-b-2 border-gray-900 w-full',
            })