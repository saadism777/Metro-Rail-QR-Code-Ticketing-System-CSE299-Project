from django.urls import path
from .views import SignUp,GeneralUserSignUpView,TrainMasterSignUpView
urlpatterns = [
path('signup/',SignUp,name='signup'),
  path('accounts/signup/guser/', GeneralUserSignUpView.as_view(), name='guser_signup'),
  path('accounts/signup/trainmaster/', TrainMasterSignUpView.as_view(), name='trainmaster_signup'),
]