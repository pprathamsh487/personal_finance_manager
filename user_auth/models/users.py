from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure email is unique
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    REQUIRED_FIELDS = ['email']  # Email will be required on top of username
    
    
    class Meta:
        db_table = 'USERS'
    def __str__(self):
        return self.username
