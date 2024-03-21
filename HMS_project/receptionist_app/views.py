
from django.core.cache import cache
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.crypto import get_random_string
from .models import PatientRegister
from admin_app.models import User
from django.db.models import Q
from django import *
from admin_app .models import UserProfileInfo2
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user = request.user
    return render(request, 'receptionist_dash/profile.html', {'user': user})

@login_required
def profile_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.user != user:  # Ensure user can only update their own profile
        return redirect('show_rece_profile')
    
    user_profile, created = UserProfileInfo2.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        user_profile.profile_pic = profile_pic
        user_profile.save()
        return redirect('show_rece_profile')
    
    return render(request, 'receptionist_dash/update_profile.html', {'user_id': user_id, 'user_profile': user_profile})


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

            
        PatientRegister.objects.create(
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
        staff=doctor_id,
                )
          
        patient_count = cache.get('patient_count', 0)
        patient_count += 1
        cache.set('patient_count', patient_count)
        messages.success(request, 'Patient data sent successfully.')  
        register=True 
    return render(request, 'receptionist_dash/add-patient.html',{'register':register,})  # Render the form template initially
def check_patient_data(request):
    patient_count = cache.get('patient_count', 0)
    patients = PatientRegister.objects.filter(is_checked=False)
    return render(request, 'doctor/unchecked_patient.html', {'patients': patients ,'patient_count': patient_count})

def check_patient(request, patient_id):
    patient = get_object_or_404(PatientRegister, patient_id=patient_id)
    patient.is_checked = True
    patient.save()
    messages.success(request, 'Patient is  checked successfully.')
    
    patient_count = cache.get('patient_count', 0)
    patient_count -= 1
    cache.set('patient_count', patient_count)
    
    return redirect('check_patient_data')


def delete_patient(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        patients = PatientRegister.objects.filter(
             Q(patient_id__icontains=search_query) |
             Q(first_name__icontains=search_query) |
             Q(middle_name__icontains=search_query) |
             Q(last_name__icontains=search_query) |
             Q(gender__icontains=search_query) |
             Q(birth_date__icontains=search_query) |
             Q(age__icontains=search_query) |
             Q(phone_number__icontains=search_query) |
             Q(email__icontains=search_query) |
             Q(country__icontains=search_query) |
             Q(city__icontains=search_query) |
             Q(region__icontains=search_query) |
             Q(kebele__icontains=search_query) |
             Q(staff__icontains=search_query)
)
        if 'delete' in request.POST:
            # Handle deletion of selected employees
            patient_delete = request.POST.getlist('patient_delete')
            PatientRegister.objects.filter(patient_id__in=patient_delete).delete()
            
    else:
        patients = PatientRegister.objects.all()

    return render(request, 'receptionist_dash/patients.html', {'patients': patients})
def dis_patient(request):
    patients = PatientRegister.objects.all()
    return render(request,'receptionist_dash/patients.html', {'patients':patients})
def about_patient(request):
    return render(request, 'receptionist_dash/about-patient.html')  # Render the form template initially
def receptionist_dash(request):
    return render(request,'receptionist_dash/receptionist_dash.html')
def receptionist_dash_content(request):
    return render(request,'receptionist_dash/dash_content.html')
# def edit_patient(request):
    # if 'update' in request.POST:
   # Handle deletion of selected employees
            #  patient_delete = request.POST.getlist('patient_delete')
            #  try:
                #  patient = PatientRegister.objects.filter(patient_id__in=patient_delete)
                #  first_name = request.POST.get('first_name')
                #  middle_name = request.POST.get('middle_name')
                #  last_name = request.POST.get('last_name')
                #  gender = request.POST.get('gender')
                #  birth_date = request.POST.get('birth_date')
                #  age = request.POST.get('age')
                #  phone_number = request.POST.get('phone_number')
                #  email = request.POST.get('email')
                #  country = request.POST.get('country')
                #  city = request.POST.get('city')
                #  region = request.POST.get('region')
                #  kebele = request.POST.get('kebele')
                #  doctor_id = request.POST.get('doctor_id')
                #  patient = PatientRegister.objects.create(
                            # first_name=first_name,
                            # middle_name=middle_name,
                            # last_name=last_name,
                            # gender=gender,
                            # birth_date=birth_date,
                            # age=age,
                            # phone_number=phone_number,
                            # email=email,
                            # country=country,
                            # city=city,
                            # region=region,
                            # kebele=kebele,
                            # staff=doctor_id,)
                            #   
                #  patient.save()   
# 
                #  return redirect('dis_patient')
            #  except PatientRegister.DoesNotExist:
                #  pass
    # 
    # return redirect('dis_patient')
def edit_patient(request,patient_id):
     try:
       patientid = get_object_or_404(PatientRegister, pk=patient_id)
 #   std = Student.objects.get(pk=roll)
       return render(request,'receptionist_dash/edit-patient.html',{'patientid':patientid})
     except PatientRegister.DoesNotExist:
       return render(request,'receptionist_dash/edit-patient.html',{'message':'patient  not found'})
     
 
    # return render(request,'receptionist_dash/edit-patient.html')
def dis_forms(request):
    return render(request,'receptionist_dash/form.html')
def update_patient(request,patient_id):
   first_name = request.POST.get('first_name')
   middle_name = request.POST.get('middle_name')
   last_name = request.POST.get('last_name')
   age = request.POST.get('age')
   phone_number = request.POST.get('phone_number')
   email = request.POST.get('email')
   country = request.POST.get('country')
   city = request.POST.get('city')
   region = request.POST.get('region')
   kebele = request.POST.get('kebele')
   doctor_id = request.POST.get('doctor_id')
   
   patient = PatientRegister.objects.get(pk=patient_id)
   patient.first_name=first_name
   patient.middle_name=middle_name
   patient.last_name=last_name
   patient.age=age
   patient.phone_number=phone_number
   patient.email=email
   patient.country=country
   patient.city=city
   patient.region=region
   patient.kebele=kebele
   patient.staff=doctor_id
   patient.save()
   return redirect('dis_patient')
# def update(request,roll):
    # try:
        # std = get_object_or_404(Student, pk=roll)
      #std = Student.objects.get(pk=roll)
        # return render(request,'secondapp/update.html',{'std':std})
    # except Student.DoesNotExist:
        #   return render(request,'secondapp/update.html',{'message':'Student not found'})
# def do_update(request ,roll):
    # std_roll = request.POST.get('roll')
    # std_name = request.POST.get('name')
    # std_email = request.POST.get('email')
    # std_address = request.POST.get('address')
    # std_phone = request.POST.get('phone')
# 
    # std = Student.objects.get(pk=roll)
    # std.roll = std_roll
    # std.name = std_name
    # std.email = std_email
    # std.address = std_address
    # std.phone = std_phone
    # std.save()
    # return redirect('home')