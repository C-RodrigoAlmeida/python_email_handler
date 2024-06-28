from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    employee_id = models.CharField(alpha_numeric_only=True, max_length=4, unique=True, db_index=True)