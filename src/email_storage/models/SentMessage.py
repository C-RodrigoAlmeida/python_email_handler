from django.db import models
from django.db.models import Q
from email_storage.models.group import Group
from email_storage.models.recipient import Recipient
from src.core.base_model import BaseModel

class SentMessage(BaseModel):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    recipients = models.ManyToManyField(Recipient, related_name="messages")
    groups = models.ManyToManyField(Group, related_name="messages")

    class Meta:
        constraints = [
            models.CheckConstraint(
            check=Q(groups__isnull=False) | Q(recipients__isnull=False),
            name="group_or_recipient")
        ]

    def __str__(self) -> str:
        return self.subject