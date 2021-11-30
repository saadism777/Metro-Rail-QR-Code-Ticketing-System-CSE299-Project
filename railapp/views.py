from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    return render(request, 'railapp/home.html')
def ContactUs(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return redirect ('confirmation')
    return render(request, 'railapp/contact.html')
def checkout(request):
    return render(request, 'railapp/checkout.html')
def Confirmation(request):
    return render(request, 'railapp/confirmation.html')
def faq(request):
    return render(request, 'railapp/faq.html')
