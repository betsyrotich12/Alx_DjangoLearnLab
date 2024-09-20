from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    bio = models.TextField(max_length=200)
    profile_picture = models.ImageField(null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followers_users' )
    following = models.ManyToManyField('self', symmetrical=False, related_name='following_users')

    def follow(self, user):
        self.following.add(user)

    def unfollow(self, user):
        self.following.remove(user)

    def is_following(self, user):
        return self.following.filter(id=user.id).exists()
    
    def is_followed_by(self, user):
         return self.following.filter(id=user.id).exists()

