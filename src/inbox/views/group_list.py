from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from src.inbox.models.group import Group
from src.user.models.custom_user import CustomUser

class GroupListView(ListView, LoginRequiredMixin):
    model = Group
    template_name = 'group_list.html'
    context_object_name = 'rows'
    paginate_by = 10

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied
        
        custom_user = get_object_or_404(CustomUser, id=self.request.user.id)
        search = self.request.GET.get('search', '')

        queryset = Group.objects.filter(
            Q(group_owner=self.request.user) & 
            Q(deleted_at__isnull=True)
        ).order_by('name')

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | 
                Q(description__icontains=search)
            )
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        queryset = self.get_queryset()
        
        context['custom_user'] = self.request.user
        context['title'] = "Group List"
        context['headers'] = ['name', 'description', 'action']
        context['table_url'] = 'inbox:group_list'

        paginator = Paginator(queryset, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            groups = paginator.page(page)
        except PageNotAnInteger:
            groups = paginator.page(1)
        except EmptyPage:
            groups = paginator.page(paginator.num_pages)
        
        context['controls'] = groups

        search = self.request.GET.get('search', '')
        if search:
            context['search'] = search

        return context
