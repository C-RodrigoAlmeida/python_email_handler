from django import forms
from src.inbox.forms.group_baseform import GroupBaseForm
from src.inbox.models.group import Group
from src.inbox.models.recipient import Recipient

class GroupUpdateForm(GroupBaseForm):
    not_included_recipients = forms.ModelMultipleChoiceField(
        queryset=Recipient.objects.none(),
        required=False,
        label="Recipients Not in Group",
        widget=forms.CheckboxSelectMultiple
    )
    class Meta(GroupBaseForm.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.user:
            all_recipients = Recipient.objects.filter(
                contact_owner=self.user,
                deleted_at__isnull=True
            ).order_by('id')

        if self.instance and self.instance.pk:
            self.fields['recipients'].queryset = self.instance.recipients.all()
            self.fields['recipients'].required = False
            self.fields['recipients'].initial = []

            self.fields['not_included_recipients'].queryset = all_recipients.exclude(id__in=self.instance.recipients.all())

    def save(self, commit:bool = True) -> Group:
        instance = super().save(commit=False)

        recipients = self.cleaned_data.get('recipients')
        if recipients:
            instance.save() 
            instance.recipients.remove(*recipients)

        not_included_recipients = self.cleaned_data.get('not_included_recipients')
        if not_included_recipients:
            instance.save()
            instance.recipients.add(*not_included_recipients)

        if commit:
            instance.save()
        return instance