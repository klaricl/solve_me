from django.db import models

# Create your models here.

class AppUsers(models.Model):
    username = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    token = models.CharField(max_length = 32)