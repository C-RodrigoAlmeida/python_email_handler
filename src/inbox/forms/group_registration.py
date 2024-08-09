from src.inbox.forms.group_baseform import GroupBaseForm
from src.inbox.models.group import Group
from src.inbox.models.recipient import Recipient

class GroupRegistrationForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.user:
            self.fields['recipients'].queryset = Recipient.objects.filter(
                contact_owner=self.user,
                deleted_at__isnull=True
            ).order_by('id')

    def save(self, commit=True) -> Group:
        instance = super().save(commit=False)
        instance.group_owner = self.user
        if commit:
            instance.save()
        return instance