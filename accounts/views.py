from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import login
# Create your views here.


from django.views.generic import CreateView

from .forms import GeneralUserSignUpForm,TrainMasterSignUpForm
from .models import User,GeneralUser

def SignUp(request):
	return render(request,'register.html')





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

