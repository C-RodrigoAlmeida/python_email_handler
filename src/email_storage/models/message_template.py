from django.db import models
from src.core.base_model import BaseModel

class MessageTemplate(BaseModel):
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self) -> str:
        return self.subject