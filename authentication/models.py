from django.db import models
from django.contrib.auth.models import AbstractUser 
class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_photo = models.ImageField()
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
