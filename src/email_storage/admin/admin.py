from django.contrib import admin
from src.email_storage.models.sent_message import SentMessage
from src.email_storage.models.group import Group
from src.email_storage.models.recipient import Recipient
from src.email_storage.models.message_template import MessageTemplate
# Register your models here.

admin.site.register(SentMessage)
admin.site.register(Group)
admin.site.register(Recipient)
admin.site.register(MessageTemplate)