from contextlib import nullcontext
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Avatares(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatares", null=True, blank=True)