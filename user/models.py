from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

STATUS = (
    ('online', 'online'),
    ('sleeping', 'sleeping'),
    ('not online', 'not online')
)


class User(AbstractUser):
    """User model"""
    username = models.CharField(max_length=24, default='user')
    image = models.ImageField(upload_to='users/images/')
    tag = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=12 ,choices=STATUS)
    USERNAME_FIELD = 'tag'
    REQUIRED_FIELDS = ['username', 'email']


    def save(self, *args, **kwargs):
 
        if not self.tag.startswith("@"):
            self.tag = "@" + self.tag
        
        super().save(*args, **kwargs)
