from typing import Any
from django.urls import reverse_lazy
from django.views.generic import CreateView
from src.inbox.forms.recipient_registration import RecipientRegistrationForm
from src.inbox.models.recipient import Recipient



class RecipientCreateView(CreateView):
    model = Recipient
    form_class = RecipientRegistrationForm
    template_name = "recipient_management.html"
    success_url = reverse_lazy('inbox:recipient_registration')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['operation_name'] = 'Register Recipient'
        context['button_value'] = 'Register'
        return context

    def get_form_kwargs(self):
        kwargs = super(RecipientCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs