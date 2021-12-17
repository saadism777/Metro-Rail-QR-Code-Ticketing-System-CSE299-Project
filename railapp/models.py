from django.db import models
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

    def save(self, *args, **kwargs):
        super(Questions, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_text = models.TextField()
    is_anonymous = models.BooleanField(default=False)

    def __unicode__(self):
        return self.id

class Announcement(models.Model):
    title = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
         ordering = ['created_on']

    def __str__(self):
        return self.title 