from src.inbox.models.message_template import MessageTemplate
from django.db.models import Q
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

class MessageTemplatesListView(ListView, LoginRequiredMixin):
    model = MessageTemplate
    template_name = "object_list.html"
    context_object_name = "rows"
    paginate_by = 10

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied
        
        search = self.request.GET.get('search', '')
        if search:
            return MessageTemplate.objects.filter(
                Q(message_owner=self.request.user) 
                & Q(deleted_at__isnull=True) 
                & (Q(subject__icontains=search) 
                   | Q(description__icontains=search))
            ).order_by('subject')

        return MessageTemplate.objects.filter(Q(message_owner=self.request.user) & Q(deleted_at__isnull=True) ).order_by('subject')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        context['custom_user'] = self.request.user
        context['title'] = "Message Template List"
        context['headers'] = ['subject', 'description', 'action']
        context['table_url'] = 'inbox:message_template_list'
        context['row_update'] = "inbox:message_template_update"
        context['row_delete'] = "inbox:message_template_delete"

        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        search = self.request.GET.get('search', '')
        if search:
            context['search'] = search
        
        try:
            context['controls'] = paginator.page(page)
        except PageNotAnInteger:
            context['controls'] = paginator.page(1)
        except EmptyPage:
            context['controls'] = paginator.page(paginator.num_pages)

        return context
