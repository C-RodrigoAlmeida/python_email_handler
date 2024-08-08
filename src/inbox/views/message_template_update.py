from typing import Any
from src.inbox.models.message_template import MessageTemplate
from src.inbox.forms.message_update import MessageUpdateForm
from django.views.generic import UpdateView

class MessageTemplateUpdateView(UpdateView):
    model = MessageTemplate
    form_class = MessageUpdateForm
    template_name = 'message_template_management.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['template_topic'] = 'Edit Message Template'
        context['template_button'] = 'Save'
        return context