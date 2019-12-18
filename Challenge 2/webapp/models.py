from django.db import models

class users(models.Model):

    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
# Create your models here.
