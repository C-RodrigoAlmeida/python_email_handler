from django.db import models
from src.inbox.models.recipient import Recipient
from src.core.base_model import BaseModel

class Group(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)    
    recipients = models.ManyToManyField(Recipient, related_name="group_recipients")
    group_owner = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='group_owner', db_index=True)
    
    def __str__(self) -> str:
        return self.name