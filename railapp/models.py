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