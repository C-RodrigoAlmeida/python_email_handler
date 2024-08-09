from django import forms
from src.inbox.forms.group_baseform import GroupBaseForm
from src.inbox.models.group import Group
from src.inbox.models.recipient import Recipient

class GroupUpdateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['not_included_recipients'] = forms.ModelMultipleChoiceField(
            queryset=Recipient.objects.only(
                'id', 'name', 'last_name', 'employee_id').filter(
                    contact_owner=self.user,
                    deleted_at__isnull=True
                ).exclude(id__in=self.instance.recipients.all()
            ).order_by('name'),
            required=False,
            label="Recipients Not in Group",
            widget=forms.CheckboxSelectMultiple
        )
        
        self.fields['recipients'] = forms.MultipleChoiceField(
            choices=((_choice.id, str(_choice)) for _choice in self.instance.recipients.only('id', 'name', 'last_name',  'employee_id').all().order_by('name')),
            required=False,
            label="Recipients in Group",
            widget=forms.CheckboxSelectMultiple
        )


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