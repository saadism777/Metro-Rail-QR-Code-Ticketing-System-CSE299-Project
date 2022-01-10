from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from django.forms import TextInput, NumberInput, EmailInput, PasswordInput, Select, FileInput
from django.db import transaction

from .models import GeneralUser, User, TrainMaster,Book

#General User Form
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

#Train Master Form
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

        return user

#Order Form
class OrderForm(ModelForm):
    class Meta:
        model = Book
        fields = ['routeid','nos']
        widgets = {
            'routeid': forms.NumberInput(attrs={'class':'form-control'}),
            'nos': forms.NumberInput(attrs={'class':'form-control'})
        }

#User Update Form
class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last_name'}),
        }
#General User Update Form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = GeneralUser
        fields = ('phone_number', 'location')
        widgets = {
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            
        }
#TrainMaster User Update Form
class ProfileUpdateFormTrainMaster(forms.ModelForm):
    
    class Meta:
        model = TrainMaster
        fields = ('phone', 'location','licenseNumber')
        widgets = {
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            'licenseNumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'License Number'}),
            
        }
