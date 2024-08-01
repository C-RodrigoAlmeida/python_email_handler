from django.urls import path
from src.inbox.views.message_template import MessageTemplateCreateView

app_name = "inbox"

urlpatterns = [
    path('message/template_creaton/', MessageTemplateCreateView.as_view(), name='message_template_creation'),
]