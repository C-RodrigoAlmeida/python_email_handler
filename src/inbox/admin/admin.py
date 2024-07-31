from django.contrib import admin
from src.inbox.models.sent_message import SentMessage
from src.inbox.models.group import Group
from src.inbox.models.recipient import Recipient
from src.inbox.models.message_template import MessageTemplate
# Register your models here.

admin.site.register(SentMessage)
admin.site.register(Group)
admin.site.register(Recipient)
admin.site.register(MessageTemplate)