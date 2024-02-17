from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def User(request):
    return render(request, 'UserAccount.html')

def patient(request):
    return render(request, 'Patient.html')

def bed(request):
    return render(request, 'Bed.html')

def prescription(request):
    return render(request, 'Prescription.html')

def service(request):
    return render(request, 'Service.html')

def login(request):
    return render(request, 'Login.html')


