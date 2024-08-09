from django import forms
from src.inbox.models.group import Group
from src.inbox.models.recipient import Recipient

class GroupRegistrationForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description', 'recipients']


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'name' or field_name == 'description':
                field.widget.attrs.update({
                    'class': 'form-control backdrop-blur bg-[#202c33] mb-8 border-b-2 border-gray-300 w-full focus:outline-none focus:border-teal-800',
                })
            else:
                field.widget.attrs.update({
                    'class': 'form-control backdrop-blur bg-[#202c33] mb-8 border-2 border-gray-300 w-full h-96 focus:outline-none focus:border-teal-800',
                })
                
    def save(self, commit=True) -> Group:
        instance = super().save(commit=False)
        instance.group_owner = self.user
        if commit:
            instance.save()
        return instance