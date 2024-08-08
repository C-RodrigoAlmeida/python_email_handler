from django import forms
from src.inbox.models.group import Group
from src.inbox.models.recipient import Recipient

class GroupRegistrationForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description', 'recipients']

    def save(self, commit=True) -> Group:
        instance = super().save(commit=False)
        instance.group_owner = self.user
        if commit:
            instance.save()
        return instance