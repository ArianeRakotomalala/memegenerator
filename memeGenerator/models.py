from django.db import models
from django.contrib.auth.models import AbstractUser

class Meme(models.Model):
    theme = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.question