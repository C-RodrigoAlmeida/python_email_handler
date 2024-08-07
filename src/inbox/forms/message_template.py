from django import forms
from src.inbox.models.message_template import MessageTemplate

    
class MessageTemplateForm(forms.ModelForm):
    class Meta:
        model = MessageTemplate
        fields = ['subject', 'description','content']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(MessageTemplateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'subject' or field_name == 'description':
                field.widget.attrs.update({
                    'class': 'form-control backdrop-blur bg-[#202c33] mb-8 border-b-2 border-gray-300 w-full focus:outline-none focus:border-teal-800',
                })
            else:
                field.widget.attrs.update({
                    'class': 'form-control backdrop-blur bg-[#202c33] mb-8 border-2 border-gray-300 w-full focus:outline-none focus:border-teal-800',
                })
    
    def save(self, commit=True):
        instance = super(MessageTemplateForm, self).save(commit=False)
        instance.message_owner = self.user
        if commit:
            instance.save()
        return instance