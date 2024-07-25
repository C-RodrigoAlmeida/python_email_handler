from django import forms
from src.user.models.custom_user import CustomUser

class RegistrationForm(forms.ModelForm):
    class_inheritance = 'form-control bg-slate-800 mb-8 border-b-2 border-slate-700'
    placeholders = 'Type here'

    name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': class_inheritance,
            'placeholder': placeholders,
        }),
    )

    last_name = forms.CharField(
        label="Last Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': class_inheritance,
            'placeholder': placeholders,
        }),
    )

    email = forms.EmailField(
        label="Email",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': class_inheritance,
            'placeholder': placeholders,
        }),
    )

    username = forms.CharField(
        label="Employee ID",
        max_length=4,
        widget=forms.TextInput(attrs={
            'class': class_inheritance,
            'placeholder': placeholders,
            'style': 'text-transform: uppercase'
        }),
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': class_inheritance,
            'placeholder': placeholders,
        }),
    )

    class Meta:
        model = CustomUser
        fields = ['name', 'last_name', 'email', 'username', 'password']