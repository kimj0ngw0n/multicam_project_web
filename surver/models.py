from django.db import models
from django.conf import settings


class Surver(models.Model):
    name = models.CharField(max_length=20)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Access', related_name='survers')


class Access(models.Model):
    surver = models.ForeignKey(Surver, on_delete=models.CASCADE, related_name='surver_access')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_access')
    type = models.CharField(max_length=20, default='')


class Category(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20, default='public')
    surver = models.ForeignKey(Surver, on_delete=models.CASCADE, related_name='categories')


class Channel(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20, default='text')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='channels')


class Message(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_messages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()


class Reaction(models.Model):
    reaction = models.CharField(max_length=20, default='good')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='reactions')
