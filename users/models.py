from django.db import models
from django.contrib.auth.models import User 

class Account(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, verbose_name='name')
    email = models.CharField(max_length=250, verbose_name='email')
    datecreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

