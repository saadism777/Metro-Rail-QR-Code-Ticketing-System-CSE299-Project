from django.db import models

# Create your models here.
class User(models.Model):
    firstname=models.CharField(max_length=70)
    lastname=models.CharField(max_length=70)
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=70)
    phone=models.IntegerField()
    gender=models.CharField(max_length=6)
    password=models.CharField(max_length=70)

