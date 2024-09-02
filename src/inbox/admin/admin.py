from django.contrib import admin
from src.inbox.models.sent_message import SentMessage
from src.inbox.models.group import Group
from src.inbox.models.recipient import Recipient
from src.inbox.models.message_template import MessageTemplate
# Register your models here.

class RecipientInline(admin.TabularInline):
    model = Group.recipients.through
    extra = 0 
    can_delete = True
    verbose_name = "Recipient"
    verbose_name_plural = "Recipients"

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [RecipientInline]
    list_display = ('name', 'description', 'group_owner', 'display_recipients')

    def display_recipients(self, obj):
        return ", ".join([recipient.name for recipient in obj.recipients.all()])

    display_recipients.short_description = 'Recipients'

admin.site.register(SentMessage)
admin.site.register(Recipient)
admin.site.register(MessageTemplate)