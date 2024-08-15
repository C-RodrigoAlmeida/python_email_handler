from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from src.inbox.models.message_template import MessageTemplate
from src.inbox.models.group import Group
from src.inbox.models.recipient import Recipient
from django.shortcuts import get_object_or_404

class EmailSend(TemplateView, LoginRequiredMixin):
    template_name = "email_send.html"
    success_url = reverse_lazy('inbox:email_send')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context