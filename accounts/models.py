from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    friends = models.ManyToManyField('self')
    friend_request_to = models.ManyToManyField('self', symmetrical=False, related_name='friend_request_from')


class Access(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_access')
    type = models.CharField(max_length=20)
