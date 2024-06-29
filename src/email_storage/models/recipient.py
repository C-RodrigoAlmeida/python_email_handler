from django.db import models
from src.core.base_model import BaseModel
from src.core.validators import alphanumeric

# Create your models here.
class Recipient(BaseModel):
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    employee_id = models.CharField(max_length=4, unique=True, db_index=True, validators=[alphanumeric])

    def __str__(self) -> str:
        return self.email