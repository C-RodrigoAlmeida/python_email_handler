from django.db import models
from src.core.base_model import BaseModel

class MessageTemplate(BaseModel):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    message_owner = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='message_owner', db_index=True)

    def __str__(self) -> str:
        return self.subject