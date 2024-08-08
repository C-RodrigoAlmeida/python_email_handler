from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from src.inbox.models.recipient import Recipient

class RecipientDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipient
    template_name='object_confirm_delete.html'
    success_url = reverse_lazy('inbox:recipient_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete(soft=True)
        return self.get_success_url()

    def get_success_url(self):
        return self.success_url
