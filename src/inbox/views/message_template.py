from django.views.generic import CreateView
from src.inbox.models.message_template import MessageTemplate
from src.inbox.forms.message_template import MessageTemplateForm


class MessageTemplateCreateView(CreateView):
    model = MessageTemplate
    form_class = MessageTemplateForm
    template_name = "message_template_create.html"
    success_url = "message_template_list"