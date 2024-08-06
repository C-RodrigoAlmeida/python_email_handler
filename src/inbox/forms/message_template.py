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
                field.widget.attrs.update({'class': 'block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-blue-500 focus:border-blue-500'})
            else:
                field.widget.attrs.update({'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500'})

    def save(self, commit=True):
        instance = super(MessageTemplateForm, self).save(commit=False)
        instance.message_owner = self.user
        if commit:
            instance.save()
        return instance