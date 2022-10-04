from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    id_card = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to="users", blank=True, null=True)
