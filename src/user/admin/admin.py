from django.contrib import admin
from src.user.models.custom_user import CustomUser

admin.site.register(CustomUser)