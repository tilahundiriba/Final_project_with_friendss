
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string
from .models import PatientRegister
from admin_app.models import User

def receptionist_dash(request):
    return render(request,'receptionist_dash/receptionist_dash.html')
def receptionist_dash_content(request):
    return render(request,'receptionist_dash/dash_content.html')

def add_patient(request):
    register=False
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        birth_date = request.POST.get('birth_date')
        age = request.POST.get('age')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        country = request.POST.get('country')
        city = request.POST.get('city')
        region = request.POST.get('region')
        kebele = request.POST.get('kebele')
        doctor_id = request.POST.get('doctor_id')
        generated_id = 'SH' + get_random_string(length=6, allowed_chars='1234567890')

        # if User.objects.filter(user_id=doctor_id).exists():
        #     doctor_id=request.POST.get('doctor_id')
        # else:
        #     return HttpResponse('wrong doctor id')   
            
        patient = PatientRegister.objects.create(
                patient_id=generated_id,
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                gender=gender,
                birth_date=birth_date,
                age=age,
                phone_number=phone_number,
                email=email,
                country=country,
                city=city,
                region=region,
                kebele=kebele,
                staff=doctor_id,)
                  
        patient.save()   
        register=True 
    return render(request, 'receptionist_dash/add-patient.html',{'register':register})  # Render the form template initially
from django.http import JsonResponse

def delete_patient(request, patient_id):
    if request.method == 'DELETE':
        try:
            patient = PatientRegister.objects.get(patient_id=patient_id)
            patient.delete()
            return JsonResponse({'message': 'Patient deleted successfully'})
        except PatientRegister.DoesNotExist:
            return JsonResponse({'message': 'Patient not found'}, status=404)
    
    return render(request,'receptionist_dash/patients.html')
def dis_patient(request):
    patients = PatientRegister.objects.all()
    return render(request,'receptionist_dash/patients.html', {'patients':patients})
def about_patient(request):
    return render(request, 'receptionist_dash/about-patient.html')  # Render the form template initially
def receptionist_dash(request):
    return render(request,'receptionist_dash/receptionist_dash.html')
def receptionist_dash_content(request):
    return render(request,'receptionist_dash/dash_content.html')
def edit_patient(request):
    return render(request,'receptionist_dash/edit-patient.html')
def dis_forms(request):
    return render(request,'receptionist_dash/form.html')
