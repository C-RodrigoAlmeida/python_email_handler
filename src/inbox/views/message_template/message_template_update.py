from typing import Any
from django.urls import reverse_lazy
from src.inbox.models.message_template import MessageTemplate
from src.inbox.forms.message_update import MessageUpdateForm
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class MessageTemplateUpdateView(UpdateView, LoginRequiredMixin):
    model = MessageTemplate
    form_class = MessageUpdateForm
    template_name = 'message_template_management.html'
    success_url = reverse_lazy('inbox:message_template_list')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['template_topic'] = 'Edit Message Template'
        context['template_button'] = 'Save'
        return context
    
    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def get_absolute_url(self) -> str:
        return self.success_url