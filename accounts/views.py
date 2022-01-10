
from django.shortcuts import render,redirect
from decimal import Decimal
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import login_required
import datetime
from django.views.generic import CreateView
from .forms import GeneralUserSignUpForm,TrainMasterSignUpForm,OrderForm,UserUpdateForm,ProfileUpdateForm,ProfileUpdateFormTrainMaster
from .models import User,GeneralUser,Book,Route,TrainMaster
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from railapp.views import userprofile,trainmasterprofile
from xhtml2pdf import pisa

#User Profile Update for General User
@login_required(login_url='log')
def userupdate(request):
    user_r = request.user
    gguser = GeneralUser.objects.filter(user=user_r)
    if request.method == 'POST':
        # request.user is user  data
        if user_r is not None and user_r.is_guser:
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = ProfileUpdateForm(
                request.POST, instance=request.user.generaluser)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Your account has been updated!')
                return redirect('userprofile')
    else:
       # category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        # "userprofile" model -> OneToOneField relatinon with user
        profile_form = ProfileUpdateForm(instance=request.user.generaluser)
        
        context = {
            # 'category': category,
            'user_form': user_form,
            'profile_form': profile_form,
           
        }
        return render(request, 'userupdate.html', context)

#Profile Update for Trainmaster User
@login_required(login_url='log')
def trainmaster_update(request):
    user_r = request.user
    gguser = TrainMaster.objects.filter(user=user_r)
    if request.method == 'POST':
        # request.user is user  data
        if user_r is not None and user_r.is_trainmaster:
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_formTM = ProfileUpdateFormTrainMaster(
                request.POST, instance=request.user.trainmaster)
            if user_form.is_valid() and profile_formTM.is_valid():
                user_form.save()
                profile_formTM.save()
                messages.success(request, 'Your account has been updated!')
                return redirect('trainmasterprofile')
    else:
       # category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        # "userprofile" model -> OneToOneField relatinon with user
        profile_formTM = ProfileUpdateFormTrainMaster(instance=request.user.trainmaster)
        
        context = {
            # 'category': category,
            'user_form': user_form,
            'profile_formTM': profile_formTM,
           
        }
        return render(request, 'trainmasterupdate.html', context)


#Function to generate pdf
def generatepdf(request,pkpk):
    book = Book.objects.filter(id=pkpk)
    template_path = 'invoice.html'
    context = {'book': book}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="ticket.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
        

#Registerpage or Portal
def SignUp(request):
	return render(request,'register.html')

#Login Function for General User
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

#Login Function for Trainmaster User
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

#Logout function for All User
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

#Registration of General Users
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

#Registration of Train Masters
class TrainMasterSignUpView(CreateView):
    model = User
    form_class = TrainMasterSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'trainmaster'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

#Searches Availlibility of Routes in Buy Ticket page
@login_required(login_url='log')
def search(request):
    context = {}
    if request.method == 'POST':
            p = request.POST.get('source')
            source_r= p.capitalize()
            q = request.POST.get('destination')
            dest_r = q.capitalize()
            date_r = request.POST.get('date')
            route_list = Route.objects.filter(source=source_r, dest=dest_r, date=date_r)

            if route_list:
                return render(request, 'list.html', locals())
            else:
                context["error"] = "Sorry no routes availiable"
                return render(request, 'search.html', context)
    else:
            return render(request, 'search.html')

#Creates order, an object of the book class
@login_required(login_url='log')
def createOrder(request):
    context = {}
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            id_r = form.cleaned_data['routeid']         
            seats_r = form.cleaned_data['nos']
            p = Route.objects.get(routeId=id_r)
            if p:
                if p.rem > int(seats_r):
                  username_r = request.user.username
                  email_r = request.user.email
                  source_r = p.source
                  dest_r = p.dest
                  date_r = p.date
                  time_r = p.time
                  cost = int(seats_r) * p.price
                  rem_r = p.rem - seats_r
                  Route.objects.filter(routeId=id_r).update(rem=rem_r)
                  p.rem=rem_r
                  book = Book(username=username_r,email=email_r,source=source_r,
                             dest=dest_r,date=date_r,time=time_r,
                             routeid=id_r,nos=seats_r,price=cost, status='Booked')
                  book.save()
                  return redirect('seebookings')
                else:
                  context["error"] = "Sorry select fewer number of seats"
                  return render(request, 'error.html', context)
           
    context = {'form':form}
    return render(request, 'order_form.html', context)

#Function of ticket payment system
@login_required(login_url='log')
def payment(request,pk):
    context = {}
    book = Book.objects.get(id=pk)
    form = OrderForm(instance=book)
    if request.method =='POST':
        form = OrderForm(request.POST, instance=book)
        if book.payment_status=='Not_Paid':
            Book.objects.filter(id=pk).update(payment_status='Paid',status='Confirmed',is_paid=True)
            return render(request, 'payment.html')
            
        elif book.payment_status=='Refunded':
            context["error"] = "Can not make payment. You have already cancelled this booking"
            return render(request, 'error.html', context)
            
        else :
            context["error"] = "You have already paid for this booking"
            return render(request, 'error.html', context)
        
    context = {'form':form}
    return render(request, 'order_form.html',context)

# Function for ticket cancellations
@login_required(login_url='log')
def cancellings(request,pk):
    context = {}
    book = Book.objects.get(id=pk)
    form = OrderForm(instance=book)
    if request.method =='POST':
        if book.payment_status=='Paid':
            Book.objects.filter(id=pk).update(payment_status='Refunded',status='Cancelled',is_paid=False,is_refunded=True)
            return redirect('seebookings')
        elif book.payment_status=='Not_Paid':
            context["error"] = "Booking Cancelled"
            return render(request, 'error.html', context)
            
        else :
            context["error"] = "We Have already Cancelled and Refunded for your booking"
            return render(request, 'error.html', context)
        
    context = {'form':form}
    return render(request, 'order_form.html',context)
      
#Function to see bookings
@login_required(login_url='log')
def seebookings(request,new={}):
    context = {}
    username_r = request.user.username
    book_list = Book.objects.filter(username=username_r)
    if book_list:
        return render(request, 'booklist.html', locals())
    else:
        context["error"] = "Sorry no route booked"
        return render(request, 'search.html', context)

#Function to see schedule
def schedule(request):
    date_now = datetime.datetime.now().date()
    routeList = Route.objects.filter(date=date_now)
    context = {'routeList' : routeList}
    return render(request, 'schedule.html', context)

#Function to see past schedules
def seeAll(request):
    routeList = Route.objects.all().order_by('-date')
    context = {'routeList' : routeList}
    return render(request, 'seeAll.html', context)

#Function to see seat information
def seats(request):
    date_now = datetime.datetime.now().date()
    routeList = Route.objects.filter(date=date_now)
    context = {'routeList' : routeList,
              }
    return render(request, 'seats.html', context)












