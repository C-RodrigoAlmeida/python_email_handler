from src.inbox.forms.message_baseform import MessageBaseForm
from src.inbox.models.message_template import MessageTemplate

    
class MessageTemplateForm(MessageBaseForm):
    class Meta(MessageBaseForm.Meta):
        pass

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.message_owner = self.user
        if commit:
            instance.save()
        return instance