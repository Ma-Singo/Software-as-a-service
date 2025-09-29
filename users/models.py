from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=16, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    
    