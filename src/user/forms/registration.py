# from django.forms import ModelForm
from django import forms
from src.user.models.custom_user import CustomUser

class RegistrationForm(CustomUser):
    # class Meta:
    #     model = CustomUser
    #     fields = ['employee_id','name', 'email', 'password']

    name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-slate-800 mb-8', 'placeholder': 'Name',
        }),
    )

    last_name = forms.CharField(
        label="Last Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-slate-800 mb-8', 'placeholder': 'Last Name',
        }),
    )

    email = forms.EmailField(
        label="Email",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-slate-800 mb-8', 'placeholder': 'Email',
        }),
    )

    username = forms.CharField(
        label="Employee ID",
        max_length=4,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-slate-800 mb-8', 'placeholder': 'Employee ID',
        }),
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control bg-slate-800 mb-8', 'placeholder': 'Password',
        }),
    )