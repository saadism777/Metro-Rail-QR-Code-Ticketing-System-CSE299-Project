from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import GeneralUser, User, TrainMaster

class GeneralUserSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)
    email=forms.EmailField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email=self.cleaned_data.get('email')
        user.is_guser = True
        user.save()
        guser = GeneralUser.objects.create(user=user)
        guser.phone_number=self.cleaned_data.get('phone_number')
        guser.location=self.cleaned_data.get('location')
        guser.save()
        return user


class TrainMasterSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email=forms.EmailField(required=True)
    phone=forms.CharField(required=True)
    location = forms.CharField(required=True)
    licenseNumber=forms.CharField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email=self.cleaned_data.get('email')
        user.is_trainmaster = True
        user.save()
        trainmaster = TrainMaster.objects.create(user=user)
        trainmaster.phone=self.cleaned_data.get('phone')
        trainmaster.location=self.cleaned_data.get('location')
        trainmaster.licenseNumber=self.cleaned_data.get('licenseNumber')
        
        trainmaster.save()

        return trainmaster