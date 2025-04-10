from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    receive_newsletter = models.BooleanField(default=False)
    terms = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username
