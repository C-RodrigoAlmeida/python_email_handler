from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from src.inbox.models.group import Group
from src.inbox.models.recipient import Recipient
from src.user.models.custom_user import CustomUser

class GroupListView(ListView, LoginRequiredMixin):
    model = Group
    template_name = 'group_list.html'
    context_object_name = 'groups'
    paginate_by = 10

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied
        
        self.custom_user = get_object_or_404(CustomUser, id=self.request.user.id)
        return Group.objects.filter(Q(group_owner=self.custom_user)  & Q(deleted_at__isnull=True)).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_user'] = self.custom_user
        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            context['pagination'] = paginator.page(page)
        except PageNotAnInteger:
            context['pagination'] = paginator.page(1)
        except EmptyPage:
            context['pagination'] = paginator.page(paginator.num_pages)

        return context
