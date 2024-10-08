from django.urls import path

# Message Imports
from src.inbox.views.message_template.message_template_creation import MessageTemplateCreateView
from src.inbox.views.message_template.message_template_list import MessageTemplatesListView
from src.inbox.views.message_template.message_template_update import MessageTemplateUpdateView
from src.inbox.views.message_template.message_template_delete import MessageTemplateDeleteView

# Recipient Imports
from src.inbox.views.recipient.recipient_registration import RecipientCreateView
from src.inbox.views.recipient.recipient_list import RecipientListView
from src.inbox.views.recipient.recipient_update import RecipientUpdateView
from src.inbox.views.recipient.recipient_delete import RecipientDeleteView

# Group Imports
from src.inbox.views.group.group_registration import GroupRegistrationView
from src.inbox.views.group.group_list import GroupListView
from src.inbox.views.group.group_update import GroupUpdateView
from src.inbox.views.group.group_delete import GroupDeleteView

# Email Imports
from src.inbox.views.email_send import EmailSend

app_name = "inbox"

urlpatterns = [
    # Message Template URLs
    path('message/template_creation/', MessageTemplateCreateView.as_view(), name='message_template_creation'),
    path('message/template_list/', MessageTemplatesListView.as_view(), name='message_template_list'),
    path('message/template_update/<int:pk>/', MessageTemplateUpdateView.as_view(), name='message_template_update'),
    path('message/template_delete/<int:pk>/', MessageTemplateDeleteView.as_view(), name='message_template_delete'),

    # Recipient URLs
    path('recipient/registration/', RecipientCreateView.as_view(), name='recipient_registration'),
    path('recipient/list/', RecipientListView.as_view(), name='recipient_list'),
    path('recipient/update/<int:pk>/', RecipientUpdateView.as_view(), name='recipient_update'),
    path('recipient/delete/<int:pk>/', RecipientDeleteView.as_view(), name='recipient_delete'),

    # Group URLs
    path('group/registration/', GroupRegistrationView.as_view(), name='group_registration'),
    path('group/list/', GroupListView.as_view(), name='group_list'),
    path('group/update/<int:pk>/', GroupUpdateView.as_view(), name='group_update'),
    path('group/delete/<int:pk>/', GroupDeleteView.as_view(), name='group_delete'),

    # Email URLs
    path('email/send/', EmailSend.as_view(), name='email_send'),
]