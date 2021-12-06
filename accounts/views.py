
from django.shortcuts import render,redirect
from decimal import Decimal
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView

from .forms import GeneralUserSignUpForm,TrainMasterSignUpForm,OrderForm
from .models import User,GeneralUser,Book,Route





def SignUp(request):
	return render(request,'register.html')


def log(request):
    """
    This method is used to view the login page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a search page which is a HTML page.
    :rtype: HttpResponse.
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
          if request.method == 'POST':
              username =request.POST.get('guser_name')
              password =request.POST.get('guser_password')
             
              user= authenticate(request, username=username, password=password)

              if user is not None and user.is_guser:
                  login(request, user)
                  return redirect('home')
              elif user is not None and user.is_trainmaster:
                  messages.info(request, 'This  is for general users only, You are a Train Master')
              else:
                 messages.info(request, 'Username or Password is incorrect')
            

    context= {}
    return render(request, 'login.html', context)

def log2(request):
    """
    This method is used to view the login page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a search page which is a HTML page.
    :rtype: HttpResponse.
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
          if request.method == 'POST':
              username =request.POST.get('trainmaster_name')
              password =request.POST.get('trainmaster_password')
             
              user= authenticate(request, username=username, password=password)

              if user is not None and user.is_trainmaster:
                  login(request, user)
                  return redirect('home')
              elif user is not None and user.is_guser:
                  messages.info(request, 'This  is for Train Masters only, You are a General User')
              else:
                 messages.info(request, 'Username or Password is incorrect')
            

    context= {}
    return render(request, 'login.html', context)

def log_out(request):
    """
    This method is used to logout the user and redirect them to the login page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a search page which is a HTML page.
    :rtype: HttpResponse.
    """
    logout(request)
    return redirect('log')

class GeneralUserSignUpView(CreateView):
    model = User
    form_class = GeneralUserSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'guser'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class TrainMasterSignUpView(CreateView):
    model = User
    form_class = TrainMasterSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'trainmaster'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('home')


@login_required(login_url='log')
def search(request):
    context = {}
    if request.method == 'POST':
            source_r = request.POST.get('source')
            dest_r = request.POST.get('destination')
            date_r = request.POST.get('date')
            route_list = Route.objects.filter(source=source_r, dest=dest_r, date=date_r)

            if route_list:
                return render(request, 'list.html', locals())
            else:
                context["error"] = "Sorry no routes availiable"
                return render(request, 'search.html', context)
    else:
            return render(request, 'search.html')


def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'order_form.html', context)











