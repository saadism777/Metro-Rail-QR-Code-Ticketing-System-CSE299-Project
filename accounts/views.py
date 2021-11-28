from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib import messages

from django.views.generic import CreateView

from .forms import GeneralUserSignUpForm,TrainMasterSignUpForm
from .models import User,GeneralUser

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

              if user is not None:
                  login(request, user)
                  return redirect('home')
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

