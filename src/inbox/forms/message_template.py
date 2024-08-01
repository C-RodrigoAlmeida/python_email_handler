from django.forms import ModelForm
from src.inbox.models.message_template import MessageTemplate

class MessageTemplateForm(ModelForm):
    class Meta:
        model = MessageTemplate
        fields = ['subject', 'message']