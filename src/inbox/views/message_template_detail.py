from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from src.inbox.models.message_template import MessageTemplate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from src.user.models.custom_user import CustomUser

class MessageTemplateDetailView(LoginRequiredMixin, DetailView):
    model = MessageTemplate
    template_name = "message_template_detail.html"
    context_object_name = "template"

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied

        self.custom_user = get_object_or_404(CustomUser, id=self.request.user.id)
        return MessageTemplate.objects.filter(message_owner=self.custom_user)