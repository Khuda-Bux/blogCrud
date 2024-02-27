from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100)
    dis=models.TextField()

    # Hi_Bro = models.Manager()
