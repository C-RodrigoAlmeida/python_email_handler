from django.db import models
from src.email_storage.models.recipient import Recipient
from src.core.base_model import BaseModel

class Group(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)    
    recipients = models.ManyToManyField(Recipient, related_name="groups")
    
    def __str__(self) -> str:
        return self.name