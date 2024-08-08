from src.inbox.forms.recipient_baseform import RecipientBaseForm
from src.inbox.models.recipient import Recipient

class RecipientRegistrationForm(RecipientBaseForm):
    class Meta(RecipientBaseForm.Meta):
        pass

    def save(self, commit: bool = True) -> Recipient:
        instance = super().save(commit=False)
        instance.contact_owner = self.user
        if commit:
            instance.save()
        return instance