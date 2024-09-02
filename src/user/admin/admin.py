from django.contrib import admin
from src.user.models.custom_user import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name', 'last_name', 'email')
    search_fields = ('employee_id', 'first_name', 'last_name', 'email')
    list_filter = ('is_superuser', 'is_staff', 'is_active')