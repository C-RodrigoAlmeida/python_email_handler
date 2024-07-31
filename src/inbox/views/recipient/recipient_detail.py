from inbox.models.recipient import Recipient
from django.views.generic import DetailView

class RecipientDetailView(DetailView):
    model = Recipient
    template_name = "email_storage/recipient_detail.html"
    context_object_name = "recipient"