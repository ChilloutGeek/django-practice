from django.db import models
from django.contrib.auth.models import User 

class Account(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    datecreated = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=250, default='')
    profilepic = models.ImageField(upload_to='profilepic', default='profilepic/download.jpeg')

    def __str__(self):
        return self.name


