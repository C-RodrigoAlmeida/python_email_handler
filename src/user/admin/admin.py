from django.contrib import admin
from .models.custom_user import CustomUser

admin.site.register(CustomUser)