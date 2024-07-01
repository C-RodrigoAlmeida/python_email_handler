from django.db import models
from django.contrib.auth.models import AbstractUser
from src.core.validators import alphanumeric
from src.core.base_model import BaseModel

class CustomUser(BaseModel, AbstractUser):
    username = None 
    employee_id = models.CharField(max_length=4, unique=True, db_index=True, validators=[alphanumeric])
    name = models.CharField(max_length=100, null=False)

    USERNAME_FIELD = "employee_id"
    REQUIRED_FIELDS = ["employee_id", "password"]