from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    bio = models.TextField(max_length=200)
    profile_picture = models.ImageField(null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following' )
