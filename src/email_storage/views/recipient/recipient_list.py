from email_storage.models.recipient import Recipient
from django.views.generic import ListView

class RecipientListView(ListView):
    model = Recipient
    template_name = "email_storage/recipient_list.html"
    context_object_name = "recipients"