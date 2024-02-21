# from django.db import models

# # Create your models here.
# class Users(models.Model):
#     email=models.EmailField(max_length=30)
#     password=models.CharField(max_length=50)

# class Person(models.Model):
#     first_name=models.CharField(max_length=70)
#     last_name=models.CharField(max_length=70)



# App1/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username