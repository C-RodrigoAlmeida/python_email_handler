from typing import Any
from django.views.generic import UpdateView
from src.inbox.models.recipient import Recipient
from src.inbox.forms.recipient_update import RecipientUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class RecipientUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipient
    form_class = RecipientUpdateForm
    template_name = "recipient_management.html"
    success_url = reverse_lazy('inbox:recipient_list')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['operation_name'] = 'Edit Recipient Informations'
        context['button_value'] = 'Save'
        return context

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs