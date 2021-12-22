from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from accounts.models import User
from django.contrib.auth.models import User,

class UserForm(ModelForm):
    class Meta:
        model=User
        fields =['username', 'email', 'first_name', 'last_name', 'phone_number', 'location']