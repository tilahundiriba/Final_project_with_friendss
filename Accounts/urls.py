from django.urls import path
from . import views

urlpatterns = [
       path('', views.User, name =""),
       
       path('patient', views.patient, name ="patient"),
       
       
       path('bed', views.bed, name ="bed"),
       
       
       path('prescription', views.prescription, name ="prescription"),
       
       
       path('service', views.service, name ="service"),
       
        path('login', views.login, name ="login"),
       
        
]