from typing import Any
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from src.inbox.forms.group_registration import GroupRegistrationForm
from src.inbox.models.group import Group

class GroupRegistrationView(CreateView, LoginRequiredMixin):
    model = Group
    form_class = GroupRegistrationForm
    template_name = 'group_management.html'
    success_url = reverse_lazy('group_list')

    def get_queryset(self) -> None:
        if not self.request.user.is_authenticated:
            raise PermissionDenied
        
    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['template_topic'] = 'Create Recipients Group'
        context['template_button'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.group_owner = self.request.user
        return super().form_valid(form)