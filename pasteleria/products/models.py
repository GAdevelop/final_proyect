from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='postpic', null=True, blank=True)

    

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.pk)))

