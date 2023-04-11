from django.db import models
from django.conf import settings


class Surver(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='survers')


class Category(models.Model):
    name = models.CharField(max_length=20)
    surver = models.ForeignKey(Surver, on_delete=models.CASCADE, related_name='categories')


class Channel(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='channels')


class Message(models.Model):
    channel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    reaction = models.CharField(max_length=20)
