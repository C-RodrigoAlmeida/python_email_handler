from django.urls import path
from src.inbox.views.message_template_creation import MessageTemplateCreateView
from src.inbox.views.message_template_list import MessageTemplatesListView

app_name = "inbox"

urlpatterns = [
    path('message/template_creation/', MessageTemplateCreateView.as_view(), name='message_template_creation'),
    path('message/template_list/', MessageTemplatesListView.as_view(), name='message_template_list'),
]