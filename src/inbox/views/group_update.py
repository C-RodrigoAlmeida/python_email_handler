from django.views.generic import UpdateView
from src.inbox.models.group import Group
from src.inbox.forms.group_update import GroupUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupUpdateForm
    template_name = 'group_management.html'
    success_url = reverse_lazy('inbox:group_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_topic'] = 'Edit Recipients Group'
        context['template_button'] = 'Save'
        return context

    def get_queryset(self):
        return Group.objects.prefetch_related('recipients').filter(group_owner=self.request.user)