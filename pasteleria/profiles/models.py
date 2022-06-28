from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#Costum User Model

class CostumUser(AbstractUser):
    first_name = models.CharField(max_length=40, null=True) #name
    second_name = models.CharField(max_length=40, null=True)
    role = models.TextField() #description
    linkedIn = models.URLField(max_length=200) #web link
    profile_pic = models.ImageField(upload_to='profilepic', null=True, blank=True) #image
    

