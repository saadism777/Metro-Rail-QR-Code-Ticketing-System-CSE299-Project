from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_guser = models.BooleanField(default=False)
    is_trainmaster = models.BooleanField(default=False)

class GeneralUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=300)
    location = models.CharField(max_length=500)
    email = models.EmailField(max_length=200)

    def __str__(self):
           return self.user.username


class TrainMaster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    location = models.CharField(max_length=500)
    licenseNumber = models.CharField(max_length=200)
    def __str__(self):
           return self.user.username


class Route(models.Model):
    routeId= models.AutoField(primary_key=True)
    source = models.CharField(max_length=200)
    dest = models.CharField(max_length=200)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return self.dest
class Book(models.Model):
    BOOKED = 'Booked'
    CANCELLED = 'Cancelled'
    CONFIRMED = 'Confirmed'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),
                       (CONFIRMED,'Confirmed'))

    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    routeid = models.IntegerField()
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=15)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.username



