from django.contrib import admin
from src.inbox.models.sent_message import SentMessage
from src.inbox.models.group import Group
from src.inbox.models.recipient import Recipient
from src.inbox.models.message_template import MessageTemplate

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
    search_fields = ('name', 'description')
    list_filter = ('name', 'description', 'group_owner')

    def display_recipients(self, obj):
        return ", ".join([recipient.name for recipient in obj.recipients.all()])

    display_recipients.short_description = 'Recipients'


@admin.register(SentMessage)
class SentMessageAdmin(admin.ModelAdmin):
    list_display = ('sent_by', 'subject', 'message', 'recipients', 'groups')
    search_fields = ('sent_by', 'subject', 'message', 'recipients', 'groups')
    list_filter = ('sent_by', 'subject', 'message', 'recipients', 'groups')

@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'email')
    search_fields = ('employee_id', 'name', 'email')
    list_filter = ('employee_id', 'name', 'email')

@admin.register(MessageTemplate)
class MessageTemplateAdmin(admin.ModelAdmin):
    list_display = ('subject', 'description', 'message_owner')
    search_fields = ('subject', 'description')
    list_filter = ('subject', 'description', 'message_owner')