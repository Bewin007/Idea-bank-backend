from django.db import models

# Create your models here.
class Table(models.Model):
    User = models.CharField(max_length=30)
    Title = models.CharField(max_length=50)
    Content = models.CharField(max_length=250)

    def __str__(self):
        return self.Title