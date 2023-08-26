from django.db import models


# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=10)
    nickname = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
