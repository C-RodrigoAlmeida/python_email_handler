from typing import Any
from django.urls import reverse_lazy
from django.views.generic import CreateView
from src.inbox.models.message_template import MessageTemplate
from src.inbox.forms.message_registration import MessageTemplateForm


class MessageTemplateCreateView(CreateView):
    model = MessageTemplate
    form_class = MessageTemplateForm
    template_name = "message_template_management.html"
    success_url = reverse_lazy('inbox:message_template_list')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['template_topic'] = 'Message Template Registration'
        context['template_button'] = 'Register'
        return context

    def get_form_kwargs(self):
        kwargs = super(MessageTemplateCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs