from django.contrib import admin
from .models import SentMessage, Group, Recipient, MessageTemplate

# Register your models here.

admin.site.register(SentMessage)
admin.site.register(Group)
admin.site.register(Recipient)
admin.site.register(MessageTemplate)