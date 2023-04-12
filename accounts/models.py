from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    friends = models.ManyToManyField('self', related_name='friends_from')
    friend_request_to = models.ManyToManyField('self', symmetrical=False, related_name='friend_request_from')
