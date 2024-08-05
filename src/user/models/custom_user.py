from django.db import models
from django.contrib.auth.models import AbstractUser
from src.core.validators import alphanumeric
from src.core.base_model import BaseModel
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, employee_id, password=None, **extra_fields):
        if not employee_id:
            raise ValueError('The Employee ID must be set')
        user = self.model(employee_id=employee_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, employee_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(employee_id, password, **extra_fields)

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
