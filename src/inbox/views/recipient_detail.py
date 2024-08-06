from src.inbox.models.recipient import Recipient
from src.user.models.custom_user import CustomUser
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class RecipientDetailView(DetailView):
    model = Recipient
    template_name = "recipient_detail.html"
    context_object_name = "recipient"

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied

        self.custom_user = get_object_or_404(CustomUser, id=self.request.user.id)
        return Recipient.objects.filter(contact_owner=self.custom_user)