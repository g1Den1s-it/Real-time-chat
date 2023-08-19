import random
import string
from django.db import models

from user.models import User
# Create your models here.

def set_random_custom_id():
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(24))
    return random_string


class Chat(models.Model):
    custom_id = models.CharField(max_length=24, unique=True, default=set_random_custom_id())
    name = models.CharField(max_length=24)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_chats')
    user = models.ManyToManyField(User, related_name='participant_chats')
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    chat = models.ForeignKey(Chat, to_field='custom_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:10]
