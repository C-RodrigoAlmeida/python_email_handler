from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Employee ID",
        max_length=4,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-slate-800 mb-8 border-b-2 border-slate-700',
            'style': 'text-transform: uppercase',
            'placeholder': 'Type here',

        }),
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control bg-slate-800 mb-8 border-b-2 border-slate-700', 
            'placeholder': 'Type here',
        }),
    )