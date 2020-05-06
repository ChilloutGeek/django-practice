from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=250,)
    body = models.TextField(max_length=5000,) 
    datecreated = models.DateTimeField(auto_now_add=True)
    dateupdated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

