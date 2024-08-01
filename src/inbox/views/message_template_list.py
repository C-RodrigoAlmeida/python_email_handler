from django.views.generic import ListView
from src.inbox.models.message_template import MessageTemplate

class MessageTemplatesListView(ListView):
    model = MessageTemplate
    template_name = "message_template_list.html"
    context_object_name = "templates"