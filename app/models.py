
from django.db import models
from django.core import validators

class Post(models.Model):
    name = models.CharField(max_length=255)

class Worker(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    age = models.ImageField()
    work = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="None")
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

