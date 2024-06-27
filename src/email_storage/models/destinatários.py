from django.db import models
from src.core.base_model import BaseModel

# Create your models here.
class EmailRecipients(BaseModel):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.email