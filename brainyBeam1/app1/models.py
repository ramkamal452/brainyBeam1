
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.PositiveIntegerField()

    def __str__(self):
        return self.username
