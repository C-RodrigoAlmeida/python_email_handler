from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    fields = ['employee_id', 'password']
    widgets = {
        'employee_id': forms.TextInput(attrs={'style': 'text-transform:uppercase;'}),
        'password': forms.PasswordInput()
    }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control bg-slate-800 mb-8 border-b-2 border-slate-700',
            })