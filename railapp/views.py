import collections
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.db import connection
from collections import namedtuple
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
        ques_obj = Questions.objects.all()
        ans_obj = Answers.objects.all()
        content={'ques_obj':ques_obj, 'ans_obj':ans_obj}
        return render(request, 'railapp/faq.html', content)

    
def userprofile(request):
    return render(request, 'railapp/userprofile.html')
def trainmasterprofile(request):
    return render(request, 'railapp/trainmasterprofile.html')

def TrainSchedule(request):
    context = {'is_submit': False}
    if request.method == "POST":
        train_no = request.POST.get('train-no')
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM `railapp_train` WHERE `train_no`='{train_no}'")
            train_obj =collections.namedtuplefetcall(cursor)
        if not train_obj:
            messages.error(request, 'The given Train Number does not exist.')
        else:
            context['is_submit'] = True
            train_obj = train_obj[0]
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM `railapp_trainschedule` INNER JOIN `railapp_station` ON (`railapp_trainschedule`.`station_id` =`railapp_station`.`station_code`) WHERE `train_id`='{train_no}' ORDER BY distance ASC")
                schedule_obj =collections.namedtuplefetchall(cursor)
            context['train'] = train_obj
            context['schedules'] = schedule_obj
    return render(request, 'railapp/trainschedule.html')
