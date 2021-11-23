from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    return render(request, 'railapp/home.html')
def reg(request):
    return render(request, 'railapp/registration.html')
def log(request):
    return render(request, 'railapp/login.html')