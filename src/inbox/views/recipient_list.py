from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from src.inbox.models.recipient import Recipient
from src.user.models.custom_user import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

class RecipientListView(LoginRequiredMixin, ListView):
    model = Recipient
    template_name = "recipient_list.html"
    context_object_name = "recipients"
    paginate_by = 10

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied
        
        self.custom_user = get_object_or_404(CustomUser, id=self.request.user.id)
        return Recipient.objects.filter(contact_owner=self.custom_user).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_user'] = self.custom_user
        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            context['recipients'] = paginator.page(page)
        except PageNotAnInteger:
            context['recipients'] = paginator.page(1)
        except EmptyPage:
            context['recipients'] = paginator.page(paginator.num_pages)

        return context
