from django.forms import ModelForm
from src.inbox.models.message_template import MessageTemplate

class MessageTemplateForm(ModelForm):
    class Meta:
        model = MessageTemplate
        fields = ['subject', 'message']

    def __init__(self, *args, **kwargs):
        super(MessageTemplateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control mb-8 border-b-2 border-green-900',
            })
