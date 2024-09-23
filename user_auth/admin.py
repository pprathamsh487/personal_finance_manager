from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.users import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'phone_number', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
