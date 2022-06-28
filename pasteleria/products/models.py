from django.db import models
#from profiles.models import CostumUser

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    body = models.TextField()
    #author = models.ForeignKey(CostumUser, on_delete=models.CASCADE, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='postpic', null=True, blank=True)

    

    def __str__(self):
        return self.title

