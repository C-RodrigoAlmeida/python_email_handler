from django import forms
from src.inbox.models.group import Group

class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description', 'recipients']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        
        self.fields['recipients'].widget = forms.CheckboxSelectMultiple()

        for field_name, field in self.fields.items():
            if field_name == 'name' or field_name == 'description':
                field.widget.attrs.update({
                    'class': 'form-control backdrop-blur bg-[#202c33] mb-8 border-b-2 border-gray-300 w-full focus:outline-none focus:border-teal-800',
                })
            else:
                field.widget.attrs.update({
                    'class': 'form-control',
                })