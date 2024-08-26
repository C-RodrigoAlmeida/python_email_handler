from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from src.inbox.models.message_template import MessageTemplate
from src.inbox.models.group import Group
from src.inbox.models.recipient import Recipient

class EmailSend(TemplateView, LoginRequiredMixin):
    template_name = "email_send.html"
    success_url = reverse_lazy('inbox:email_send')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.GET.get('email_type') == 'template':
            context['templates'] = MessageTemplate.objects.filter(
                message_owner=self.request.user,
                deleted_at__isnull=True
            ).order_by('subject')    
            
        if self.request.GET.get('cc_type') == 'recipients' or self.request.GET.get('recipient_type') == 'recipients':
            context['cc_recipients'] = Recipient.objects.filter(
                contact_onwer=self.request.user,
                deleted_at__isnull=True
            ).order_by('name')

        if self.request.GET.get('cc_type') == 'groups' or self.request.GET.get('recipient_type') == 'groups':
            context['cc_groups'] = Group.objects.filter(
                group_owner=self.request.user,
                deleted_at__isnull=True
            ).order_by('name')

        return context