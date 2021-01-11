from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Note(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(max_length=1000, blank=True, null=True)

def __str__(self):
    return self.title

# def __str(self):
#     return self.body

