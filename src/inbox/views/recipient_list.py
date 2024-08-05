from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from src.inbox.models.recipient import Recipient
from src.user.models.custom_user import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class RecipientListView(LoginRequiredMixin, ListView):
    model = Recipient
    template_name = "recipient_list.html"
    context_object_name = "recipients"

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied

        self.custom_user = get_object_or_404(CustomUser, id=self.request.user.id)
        return Recipient.objects.filter(contact_owner=self.custom_user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_user'] = self.custom_user
        return context
