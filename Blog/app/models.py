from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Table(models.Model):
    User = models.CharField(max_length=30, blank=False, default='')
    Title = models.CharField(max_length=50, blank=False, default='')
    Content = models.CharField(max_length=250, blank=False, default='')

    def __str__(self):
        return self.Title

class User(models.Model):
    username = models.CharField(max_length=255, blank=False, default='')
    email = models.CharField(max_length=255, blank=False, default='')
    password = models.CharField(max_length=65, blank=False, default='')
    
    def __str__(self):
        return self.Name

