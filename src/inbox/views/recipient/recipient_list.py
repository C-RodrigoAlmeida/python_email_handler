from django.views.generic import ListView
from src.inbox.models.recipient import Recipient
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.db.models import Q

class RecipientListView(LoginRequiredMixin, ListView):
    model = Recipient
    template_name = "object_list.html"
    context_object_name = "rows"
    paginate_by = 10

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        if search:
            return Recipient.objects.filter(
                Q(contact_owner=self.request.user) 
                & Q(deleted_at__isnull=True) 
                & (Q(name__icontains=search) 
                   | Q(last_name__icontains=search) 
                   | Q(email__icontains=search) 
                    |Q(employee_id__icontains=search))
            ).order_by('name')
        else:
            return Recipient.objects.filter(Q(contact_owner=self.request.user) & Q(deleted_at__isnull=True)).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["custom_user"] = self.request.user
        context["title"] = "Group List"
        context["headers"] = ["employee_id", "name", "last_name", "email", "action"]
        context["table_url"] = "inbox:recipient_list"
        context["row_update"] = "inbox:recipient_update"
        context["row_delete"] = "inbox:recipient_delete"

        search = self.request.GET.get('search', '')
        if search:
            context['search'] = search


        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            context['controls'] = paginator.page(page)
        except PageNotAnInteger:
            context['controls'] = paginator.page(1)
        except EmptyPage:
            context['controls'] = paginator.page(paginator.num_pages)

        return context
