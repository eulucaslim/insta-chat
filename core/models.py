from django.db import models

class Follower(models.Model):
    username = models.CharField(max_length=50, unique=True)
    insta_id = models.CharField(max_length=60)

class ChatUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    insta_id = models.CharField(max_length=60)
    followers = models.ManyToManyField(Follower)
