
from django.core.cache import cache
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.crypto import get_random_string
from .models import PatientRegister
from admin_app.models import User,Notification,UserProfileInfo
from django.db.models import Q
from django import *
from doctor_app.models import PatientHistory
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .utils import generate_password,generate_username
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from HMS_project import settings
from twilio.rest import Client
from django.http import HttpResponse

from twilio.base.exceptions import TwilioRestException
def doctor_list(request):
    # Get all distinct doctor IDs from the PatientHistory model
    doctor_ids = PatientHistory.objects.values_list('Doctor_ID', flat=True).distinct()

    doctors_with_specialty = []
    for doctor_id in doctor_ids:
        # Get the doctor user object using the doctor ID
        doctor = User.objects.get(pk=doctor_id)

        # Get the doctor's specialty from UserInfo2 table
        try:
            specialty = doctor.userprofileinfo.specialty
        except UserProfileInfo.DoesNotExist:
            specialty = None

        # Count the number of untested tests assigned to the doctor
        untested_test_count = PatientHistory.objects.filter(Doctor_ID=doctor_id, Is_checked=False).count()

        # If there are no untested tests, set the test count to 0
        test_count = untested_test_count if untested_test_count > 0 else 0

        doctors_with_specialty.append((doctor, specialty, test_count))
    
    return render(request, 'receptionist_dash/doctor_lists.html', {'doctors_with_specialty': doctors_with_specialty})

@login_required
def rece_profile(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    user = request.user
    return render(request, 'receptionist_dash/profile.html', {'user': user,
                                                              'notifications':notifications,
                                                              'unseen_count':unseen_count})

@login_required
def rece_profile_update(request, user_id):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    user = get_object_or_404(User, pk=user_id)
    if request.user != user:  # Ensure user can only update their own profile
        return redirect('show_rece_profile')

    user_profile, created = UserProfileInfo.objects.get_or_create(user=user)

    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        user_profile.profile_pic = profile_pic
        user_profile.save()
        return redirect('show_rece_profile')

    return render(request, 'receptionist_dash/update_profile.html', {'user_id': user_id,
                                                                      'user_profile': user_profile
                                                                      ,
                                                              'notifications':notifications,
                                                              'unseen_count':unseen_count})


def receptionist_dash(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request,'receptionist_dash/receptionist_dash.html',{
                                                              'notifications':notifications,
                                                              'unseen_count':unseen_count})
def receptionist_dash_content(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request,'receptionist_dash/dash_content.html',{
                                                              'notifications':notifications,
                                                              'unseen_count':unseen_count})

def add_patient(request):
    doctors = User.objects.filter(userprofileinfo__role='doctor')
    recep = User.objects.filter(userprofileinfo__role='receptionist')
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    register=False
    doctor_ids = PatientHistory.objects.values_list('Doctor_ID', flat=True).distinct()

    doctors_with_specialty = []
    for doctor_id in doctor_ids:
        # Get the doctor user object using the doctor ID
        doctor = User.objects.get(pk=doctor_id)

        # Get the doctor's specialty from UserInfo2 table
        try:
            specialty = doctor.userprofileinfo.specialty
        except UserProfileInfo.DoesNotExist:
            specialty = None

        # Count the number of untested tests assigned to the doctor
        untested_test_count = PatientHistory.objects.filter(Doctor_ID=doctor_id, Is_checked=False).count()

        # If there are no untested tests, set the test count to 0
        test_count = untested_test_count if untested_test_count > 0 else 0

        doctors_with_specialty.append((doctor, specialty, test_count))
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
        recep_name = request.POST.get('rece_name')
        doctor_name = request.POST.get('assidoc')
        symptom = request.POST.get('symptom')
        generated_id = 'SH' + get_random_string(length=6, allowed_chars='1234567890')

        recept = get_object_or_404(User, username=recep_name)
        doctor = get_object_or_404(User, username=doctor_name)
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
        receptinist_name=recept,
        doctor_name=doctor,
        symptom=symptom,
                )
        username = generate_username(first_name, middle_name)
        password = generate_password()
        login_credencials = 'Hello Customer!\n' + ' Your Username is:' + username  + '\nPassword is:' + password 

        # Create the user
        hashed_password = make_password(password)
        user = User.objects.create_user(username=username,
                                        password=password)

        # Create user profile
        user_profile = UserProfileInfo.objects.create(
            user=user
  
        )
        # Send email with username and password
        context = {
            'first_name':first_name,
            'middle_name':middle_name,
            'username': username,
            'password': password
           
        }
        html_message = render_to_string('receptionist_dash/email_tamplates.html', context)
        plain_message = strip_tags(html_message)
        send_mail(
            'Account Created',
            plain_message,
            settings.EMAIL_HOST_USER,
            [email],
            html_message=html_message,
            fail_silently=False,
        )
        patient_count = cache.get('patient_count', 0)
        patient_count += 1
        cache.set('patient_count', patient_count)
        messages.success(request, 'Patient data sent successfully.')
        if phone_number.startswith('0'):
            phone_number = '+251' + phone_number[1:]

        # Twilio credentials
        account_sid = 'AC853cc8d20b814ed3b23041aab29acec4'
        auth_token = 'f3d400b45cf9e9a461e3cd14ad51716c'
        twilio_number = '+19474652604'

        # Initialize Twilio client
        client = Client(account_sid, auth_token)

        try:
            # Send SMS
            message = client.messages.create(
                body=login_credencials,
                from_=twilio_number,
                to=phone_number
            )

            # Save sent message to database
            return redirect('add_patient')
        except TwilioRestException as e:
            error_message = f'Twilio Error: {e.msg}'
            # return HttpResponse(error_message)
        register=True
    return render(request, 'receptionist_dash/add-patient.html',{'register':register,
                                                                 'doctors':doctors,
                                                                 'receps':recep
                                                                 ,
                                                              'notifications':notifications,
                                                              'unseen_count':unseen_count,
                                                              'doctors_with_specialty':doctors_with_specialty})  # Render the form template initially
def check_patient_data(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    patient_count = cache.get('patient_count', 0)
    patients = PatientRegister.objects.filter(is_checked=False)
    return render(request, 'doctor/unchecked_patient.html', {'patients': patients 
                                                             ,'patient_count': patient_count
                                                             ,
                                                              'notifications':notifications,
                                                              'unseen_count':unseen_count})

def check_patient(request, patient_id):
    patient = get_object_or_404(PatientRegister, patient_id=patient_id)
    patient.is_checked = True
    patient.save()
    messages.success(request, 'Patient is  checked successfully.')

    patient_count = cache.get('patient_count', 0)
    patient_count -= 1
    cache.set('patient_count', patient_count)

    return redirect('check_patient_data')


def existing_patient(request):
    
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    form=False
    if request.method == 'POST':
        doctors = User.objects.filter(userprofileinfo2__role='doctor')
        recep = User.objects.filter(userprofileinfo2__role='receptionist')
        patient_id = request.POST.get('patient_id')
        patient = get_object_or_404(PatientRegister, patient_id=patient_id)
        form=True
        return render(request, 'receptionist_dash/existing_patient.html', {'patients': patient,
                                                                           'doctors':doctors,
                                                                           'receps':recep,
                                                                           'form':form
                                                                           ,
                                                              'notifications':notifications,
                                                              'unseen_count':unseen_count})
    return render(request, 'receptionist_dash/existing_patient.html', {'form': form,
                                                              'notifications':notifications,
                                                              'unseen_count':unseen_count})
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
             Q(kebele__icontains=search_query) 
            
)
        if 'delete' in request.POST:
            # Handle deletion of selected employees
            patient_delete = request.POST.getlist('patient_delete')
            PatientRegister.objects.filter(patient_id__in=patient_delete).delete()

    else:
        patients = PatientRegister.objects.all()

    return render(request, 'receptionist_dash/patients.html', {'patients': patients
                                                               })
def dis_patient(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    patients = PatientRegister.objects.all()
    return render(request,'receptionist_dash/patients.html', {'patients':patients
                                                              ,
                                                              'notifications':notifications,
                                                              'unseen_count':unseen_count})
def about_patient(request):
    return render(request, 'receptionist_dash/about-patient.html')  # Render the form template initially
def edit_patient(request,patient_id):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    try:
       patientid = get_object_or_404(PatientRegister, pk=patient_id)
       users= User.objects.all()
       return render(request,'receptionist_dash/edit-patient.html',{'patientid':patientid,'users':users,
                                                                    'notifications':notifications,
                                                                    'unseen_count':unseen_count})
    except PatientRegister.DoesNotExist:
       return render(request,'receptionist_dash/edit-patient.html',{'message':'patient  not found'})

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
   date = request.POST.get('birth_date')
   kebele = request.POST.get('kebele')
   doctor_id = request.POST.get('assidoc')
   rece = request.POST.get('rece_name')
   symptom = request.POST.get('symptom')
   recept = get_object_or_404(User, username=rece)
   doctor = get_object_or_404(User, username=doctor_id)
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
   patient.birth_date=date
   patient.kebele=kebele
   patient.symptom=symptom
   patient.doctor_name=doctor
   patient.receptinist_name=recept
   patient.save()
   return redirect('dis_patient')
