from django.db import models
from django.utils.text import slugify
from accounts.models import User,GeneralUser, TrainMaster


class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField()
    def __str__(self):
         return self.name


class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        slug = models.SlugField()
        super(Questions, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_text = models.TextField()
    is_anonymous = models.BooleanField(default=False)

    class Meta:
        order_with_respect_to = 'question'


    def __unicode__(self):
        return self.id


class Station(models.Model):
    station_code = models.CharField(max_length=10, primary_key=True)
    station_name = models.CharField(max_length=30)
    # location = models.CharField
    manager = models.CharField(max_length=10, default='')
    assistant_manager = models.CharField(max_length=10, default='')
    rpf = models.CharField(max_length=10, default='')
    deputy_rpf = models.CharField(max_length=10, default='')
    head_officer = models.CharField(max_length=10, default='')
    # state = models.CharField(max_length=20, null=True)
    # zone = models.CharField(max_length=20, null=True)
    # address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.station_name} ({self.station_code})'


class Train(models.Model):
    train_no = models.CharField(max_length=5, primary_key=True)
    train_name = models.CharField(max_length=100)
    source = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='train_source')
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='train_destination')
    run_days = models.CharField(max_length=100)
    classes = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.train_no} - {self.train_name}'



class TrainSchedule(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    arrival = models.TimeField()
    departure = models.TimeField()
    distance = models.IntegerField()
    day = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.train} at {self.station}'
