from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    id_card = models.CharField(max_length=16, blank=True, null=True)
    avatar = models.ImageField(upload_to="users", blank=True, null=True)
    is_doctor = models.BooleanField(default=False)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=16)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(default=0)
