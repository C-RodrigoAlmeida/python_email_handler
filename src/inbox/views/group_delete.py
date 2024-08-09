from django.urls import reverse_lazy
from django.views.generic import DeleteView
from src.inbox.models.group import Group
from django.contrib.auth.mixins import LoginRequiredMixin

class GroupDeleteView(DeleteView, LoginRequiredMixin):    
    model = Group
    template_name = 'object_confirm_delete.html'
    success_url = reverse_lazy('inbox:group_list')
    
    def delete(self, request, *args, **kwargs) :
        self.object = self.get_object()
        self.object.delete(soft=True)
        return self.success_url
