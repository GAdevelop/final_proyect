from django.db import models

# Create your models here.

<<<<<<< HEAD
#Costum User Model

class CostumUser(AbstractUser):
    first_name = models.CharField(max_length=40, null=True) #name
    second_name = models.CharField(max_length=40, null=True)
    role = models.TextField() #description
    linkedIn = models.URLField(max_length=200) #web link
    profile_pic = models.ImageField(upload_to='profilepic', null=True, blank=True) #image
    
=======
>>>>>>> a43a5c7b513a92f3d17b2e500e63bd821069a897

