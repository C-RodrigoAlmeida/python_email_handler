import urllib.parse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from src.inbox.models.message_template import MessageTemplate
from src.inbox.models.group import Group
from src.inbox.models.recipient import Recipient

class EmailSend(TemplateView, LoginRequiredMixin):
    template_name = "email_send.html"
    success_url = reverse_lazy('inbox:email_send')

    def get(self, request, *args, **kwargs):
        query_params = request.GET.dict()  
        need_redirect = False

        referrer_url = request.META.get('HTTP_REFERER')
        referrer_url_param = {}

        if referrer_url is not None:
            referrer_url_param = urllib.parse.parse_qs(urllib.parse.urlparse(referrer_url).query)

            referrer_url_param = {k: v[0] for k, v in referrer_url_param.items()}

        merged_params = {**referrer_url_param, **query_params}

        for key, value in request.GET.items():
            if merged_params.get(key) != value:
                merged_params[key] = value
                need_redirect = True

        if need_redirect:
            encoded_params = urllib.parse.urlencode(merged_params)
            new_url = f"{reverse('inbox:email_send')}?{encoded_params}"
            return HttpResponseRedirect(new_url)

        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['fields'] = ['to', 'cc', 'bcc']

        if self.request.GET.get('content_method', None) == 'template':
            context['templates'] = MessageTemplate.objects.filter(
                message_owner=self.request.user,
                deleted_at__isnull=True
            ).order_by('subject')    
       
        to_method = self.request.GET.get('to_method', None)
        cc_method = self.request.GET.get('cc_method', None)

        if to_method == 'recipient' or cc_method == 'recipient':
            context['recipients'] = Recipient.objects.filter(
                contact_owner=self.request.user,
                deleted_at__isnull=True
            ).order_by('name')

        if to_method == 'group' or cc_method == 'group':
            context['groups'] = Group.objects.filter(
                group_owner=self.request.user,
                deleted_at__isnull=True
            ).order_by('name')

        return context