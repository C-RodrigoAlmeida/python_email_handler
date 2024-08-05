from django.forms import ModelForm
from src.inbox.models.message_template import MessageTemplate

class MessageTemplateForm(ModelForm):
    class Meta:
        model = MessageTemplate
        fields = ['subject', 'message']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(MessageTemplateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'subject':
                field.widget.attrs.update({'class': 'backdrop-blur bg-gray-300/75 mb-8 border-b-2 border-green-900'})
            else:
                field.widget.attrs.update({'class': 'backdrop-blur bg-gray-300/75 mb-8 border-2 border-green-900'})

    def save(self, commit=True):
        instance = super(MessageTemplateForm, self).save(commit=False)
        instance.contact_owner = self.user
        if commit:
            instance.save()
        return instance