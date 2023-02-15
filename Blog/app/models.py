from django.db import models

# Create your models here.
class Table(models.Model):
    User = models.CharField(max_length=30, blank=False, default='')
    Title = models.CharField(max_length=50, blank=False, default='')
    Content = models.CharField(max_length=250, blank=False, default='')

    def __str__(self):
        return self.Title