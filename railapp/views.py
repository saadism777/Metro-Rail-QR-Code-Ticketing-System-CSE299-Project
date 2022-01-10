from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from railapp import models
from accounts.models import Book, GeneralUser
from django.core.exceptions import ObjectDoesNotExist

# function for the homepage.
def home(request):
    if request.method=="POST":
        print("This is post")
        title = request.POST['title']
        content = request.POST['content']
        username = request.user.username
        print(username,title,content)
        ins = Announcement(username=username,title=title,content=content)
        ins.save()
        print("written successfully")
    try:
        post_list=Announcement.objects.order_by('created_on').reverse()
        post_list_2=Announcement.objects.latest('created_on')
        test=Book.objects.all()
        context = {'post_list':post_list, 'post_list_2':post_list_2, 'test':test}
    except ObjectDoesNotExist:
        context={}
    
    return render(request, 'railapp/home.html', context)

# function for the contact us page.
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

        #sends it as an email
        send_mail(
             'message from' + name,
             subject,
             email,
             ['anjoomopshora@gmail.com'],

        )
        return render(request, 'railapp/contact.html', {'name' : name})
    else:
        return render(request, 'railapp/contact.html',{})

# function for the checkout page.
def checkout(request):
    return render(request, 'railapp/checkout.html')

# function for the confirmation page.
def Confirmation(request):
    return render(request, 'railapp/confirmation.html')

# function for the FAQ page.
def faq(request):
    already_answers=Question.objects.filter(answered=True)
    without_answers=Question.objects.filter(answered=False)
    answer_contents=Answer.objects.all()
    context={
        'already_answers':already_answers,
        'without_answers':without_answers,
        'answer_contents':answer_contents
    }
    return render(request, 'railapp/faq.html', context)

# function for the userprofile dashboard
@login_required(login_url='log')  
def userprofile(request,new={}):
    username_r = request.user.username
    user_r = request.user
    book_list = Book.objects.filter(username=username_r)
    gguser = GeneralUser.objects.filter(user=user_r)
    context = { 'gguser':gguser, 'book_list':book_list }
    if book_list:
        return render(request, 'railapp/userprofile.html', context)
    else:
        context["error"] = "Sorry no buses booked"
        return render(request, 'railapp/userprofile.html', context)

# function for the trainmaster profile dashboard
@login_required(login_url='log')
def trainmasterprofile(request):
    return render(request, 'railapp/trainmasterprofile.html')
