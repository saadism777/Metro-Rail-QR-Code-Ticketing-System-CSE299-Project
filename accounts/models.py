from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_guser = models.BooleanField(default=False)
    is_trainmaster = models.BooleanField(default=False)

class GeneralUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
           return self.user.username


class TrainMaster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    licenseNumber = models.CharField(max_length=200)
    def __str__(self):
           return self.user.username

