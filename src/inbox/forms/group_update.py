from src.inbox.forms.group_baseform import GroupBaseForm

class GroupUpdateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
