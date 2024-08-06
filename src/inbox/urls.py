from django.urls import path
from src.inbox.views.message_template_creation import MessageTemplateCreateView
from src.inbox.views.message_template_list import MessageTemplatesListView
from src.inbox.views.message_template_detail import MessageTemplateDetailView
from src.inbox.views.recipient_registration import RecipientCreateView
from src.inbox.views.recipient_list import RecipientListView
from src.inbox.views.recipient_detail import RecipientDetailView

app_name = "inbox"

urlpatterns = [
    # Message Template URLs
    path('message/template_creation/', MessageTemplateCreateView.as_view(), name='message_template_creation'),
    path('message/template_list/', MessageTemplatesListView.as_view(), name='message_template_list'),
    path('message/template/<int:pk>/', MessageTemplateDetailView.as_view(), name='message_template_detail'),

    # Recipient URLs
    path('recipient/registration/', RecipientCreateView.as_view(), name='recipient_registration'),
    path('recipient/list/', RecipientListView.as_view(), name='recipient_list'),
    path('recipient/<int:pk>/', RecipientDetailView.as_view(), name='recipient_detail'),
]