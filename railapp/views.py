from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    return render(request, 'railapp/home.html')
def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()


        send_mail(
             'message from' + name,
             subject,
             email,
             ['anjoomopshora@gmail.com'],

        )
        return render(request, 'railapp/contact.html', {'name' : name})
    else:
        return render(request, 'railapp/contact.html',{})
def checkout(request):
    return render(request, 'railapp/checkout.html')
def Confirmation(request):
    return render(request, 'railapp/confirmation.html')
def faq(request):
    content={}
    if request.user.is_authenticated:
        user=request.user
        user.backend = 'django.contrib.core.backends.ModelBackend'
        ques_obj = Questions.objects.all
        content['userdetail'] = user
        content['questions'] = ques_obj
        ans_obj = Answers.objects.all()
        content['answers'] = ans_obj
        return render(request, 'railapp/faq.html', content)

    
def userprofile(request):
    return render(request, 'railapp/userprofile.html')
def trainmasterprofile(request):
    return render(request, 'railapp/trainmasterprofile.html')
