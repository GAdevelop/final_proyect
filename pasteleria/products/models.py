from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='postpic', null=True, blank=True)

    

    def __str__(self):
        return self.title + ' | ' + str(self.author)



class Comments(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Products, related_name='comments', on_delete=models.CASCADE, null=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.post)


