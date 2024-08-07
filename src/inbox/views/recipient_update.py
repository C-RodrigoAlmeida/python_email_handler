from django.views.generic import UpdateView
from src.inbox.models.recipient import Recipient
from src.inbox.forms.recipient_update import RecipientUpdateForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class RecipientUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipient
    form_class = RecipientUpdateForm
    template_name = "recipient_list.html"
    context_object_name = "recipients"

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied