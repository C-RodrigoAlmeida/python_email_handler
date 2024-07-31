from django.db import models
from django.contrib.auth.models import AbstractUser
from src.core.validators import alphanumeric
from src.core.base_model import BaseModel
from src.user.managers import CustomUserManager

class CustomUser(BaseModel, AbstractUser):
    username = None
    employee_id = models.CharField(max_length=4, unique=True, db_index=True, validators=[alphanumeric])

    USERNAME_FIELD = "employee_id"

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        self.username = self.employee_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.employee_id