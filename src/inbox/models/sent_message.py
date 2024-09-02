from django.db import models
from django.db.models import Q
from src.inbox.models.group import Group
from src.inbox.models.recipient import Recipient
from src.core.models.base_model import BaseModel
from django.conf import settings

class SentMessage(BaseModel):
    sent_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    recipients = models.CharField(max_length=2000)
    groups = models.CharField(max_length=2000)

    class Meta:
        constraints = [
            # models.CheckConstraint(
            #     check=Q(groups__isnull=False) | Q(recipients__isnull=False),
            #     name="group_or_recipient"
            # ),
            models.CheckConstraint(
                check=Q(sent_by__isnull=False),
                name="sentby_cantbe_null"
            ),
        ]

    def __str__(self) -> str:
        return self.subject

        