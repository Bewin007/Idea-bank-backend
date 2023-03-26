from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Table(models.Model):
    User = models.CharField(max_length=250)
    Title = models.CharField(max_length=50, blank=False)
    Content = models.TextField( blank=False)    
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    username = models.CharField(max_length=255, blank=False, default='')
    email = models.CharField(max_length=255, blank=False, default='')
    password = models.CharField(max_length=65, blank=False, default='')

class Vote(models.Model):
    user = models.CharField(max_length=50)
    blog_post = models.CharField(max_length=50)
    vote_type = models.CharField(max_length=50,choices=(('U','Upvote'),('D','Downvote')))
