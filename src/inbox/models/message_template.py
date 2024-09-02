from django.db import models
from src.core.models.base_model import BaseModel

class MessageTemplate(BaseModel):
    subject = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    content = models.TextField()
    message_owner = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='message_owner', db_index=True)

    def __str__(self) -> str:
        return self.subject