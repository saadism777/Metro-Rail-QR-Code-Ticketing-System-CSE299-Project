from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('reg/', views.reg, name="reg"),
    path('log/', views.log, name="log"),
    path('contact/', views.Contact, name="contact"),
    path('checkout/', views.checkout, name="checkout")
]