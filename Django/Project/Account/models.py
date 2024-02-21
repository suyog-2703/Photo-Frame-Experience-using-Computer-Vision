from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields you want for user registration
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    # You can add more fields if needed, such as date of birth, profile picture, etc.

    def __str__(self):
        return self.username
