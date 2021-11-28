from django.urls import path
from .views import SignUp,GeneralUserSignUpView,TrainMasterSignUpView
from . import views


urlpatterns = [
  path('signup/',SignUp,name='signup'),
  path('signin/',views.SignIn,name='signin'),
  path('log/', views.log, name="log"),
  path('accounts/signup/guser/', GeneralUserSignUpView.as_view(), name='guser_signup'),
  path('accounts/signup/trainmaster/', TrainMasterSignUpView.as_view(), name='trainmaster_signup'),
]