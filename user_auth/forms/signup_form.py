from django import forms
from django.contrib.auth.forms import UserCreationForm
from ..models.users import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')