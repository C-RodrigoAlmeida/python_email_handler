
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from src.inbox.models.recipient import Recipient
from src.user.models.custom_user import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.db.models import Q

class RecipientListView(LoginRequiredMixin, ListView):
    model = Recipient
    template_name = "recipient_list.html"
    context_object_name = "recipients"
    paginate_by = 10

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied
        self.custom_user = get_object_or_404(CustomUser, id=self.request.user.id)

        search = self.request.GET.get('search', '')
        if search:
            return Recipient.objects.filter(
                Q(contact_owner=self.custom_user) 
                & Q(deleted_at__isnull=True) 
                & (Q(name__icontains=search) 
                   | Q(last_name__icontains=search) 
                   | Q(email__icontains=search) 
                    |Q(employee_id__icontains=search))
            ).order_by('name')
        else:
            return Recipient.objects.filter(Q(contact_owner=self.custom_user) & Q(deleted_at__isnull=True)).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_user'] = self.custom_user

        search = self.request.GET.get('search', '')
        if search:
            context['search'] = search


        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            context['pagination'] = paginator.page(page)
        except PageNotAnInteger:
            context['pagination'] = paginator.page(1)
        except EmptyPage:
            context['pagination'] = paginator.page(paginator.num_pages)

        return context
