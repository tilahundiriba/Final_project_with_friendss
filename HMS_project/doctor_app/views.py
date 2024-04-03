
from django.shortcuts import render
from .models import  Appointment,Prescription,Laboratory,PatientHistory
from receptionist_app.models import PatientRegister
from django.shortcuts import get_object_or_404
from admin_app.models import UserProfileInfo2
from django.core.cache import cache
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def doc_profile(request):
    user = request.user
    return render(request, 'doctor/profile_show.html', {'user': user})

@login_required
def profile_update_doc(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.user != user:  # Ensure user can only update their own profile
        return redirect('show_doctor_profile')
    
    user_profile, created = UserProfileInfo2.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        user_profile.profile_pic = profile_pic
        user_profile.save()
        return redirect('show_doctor_profile')
    
    return render(request, 'doctor/update_profile.html', {'user_id': user_id, 'user_profile': user_profile})


def dis_dr_dash(request):
    return render(request,'doctor/dr_dash.html')
def dis_labtest(request):
    labs= Laboratory.objects.all()
    return render(request,'doctor/labtests.html',{'labs':labs})
def add_lab(request):
    users=User.objects.all()
    registered=False
    if request.method == 'POST':
        patientid = request.POST.get('patient_id')
        lab_number = request.POST.get('lab_no')
        admit_date = request.POST.get('admited_date')
        lab_type = request.POST.get('lab_type')
        doctor_name = request.POST.get('dr_name')
        # Create an instance of Appointment model and save it
        try:
            patient = get_object_or_404( PatientRegister,patient_id=patientid)
            doctor = get_object_or_404(User, username=doctor_name)
            lab = Laboratory(
                PatientID=patient,
                Admit_date=admit_date,
                Lab_number=lab_number,
                Doctor_ID=doctor,
                Lab_type=lab_type,
                # Assign values to other fields similarly
            )
            lab.save()
            request_count = cache.get('request_count', 0)
            request_count += 1
            cache.set('request_count', request_count)
            messages.success(request, 'Laboratory test sent successfully.') 
            registered=True
        except PatientRegister.DoesNotExist:
            # Handle the case where the patient is not found
            # You can add appropriate error handling or redirect to an error page
            pass
        except UserProfileInfo2.DoesNotExist:
            # Handle the case where the doctor is not found
            # You can add appropriate error handling or redirect to an error page
            pass
        return render(request,'doctor/add_lab.html',{'register':registered})
    return render(request,'doctor/add_lab.html',{'users':users})
# views for getting untested lab request and render it
def check_request(request):
    request_count = cache.get('request_count', 0)
    requests = Laboratory.objects.filter(Is_tested=False)
    return render(request, 'laboratory_dash/lab_requests.html', {'requests': requests ,'request_count': request_count})
# views for testing the lab for single patient 
def checked_request(request, patient_id):
    lab_request = get_object_or_404(Laboratory, PatientID=patient_id)
    lab_request.Is_tested = True
    lab_request.save()
    messages.success(request, 'lab. request is  tested successfully.')
    request_count = cache.get('request_count', 0)
    request_count -= 1
    cache.set('request_count', request_count)
    return redirect('check_request')
# views for getting unpayed lab request and render it
def check_payment_request(request):
    request_count = cache.get('request_count', 0)
    payments = Laboratory.objects.filter(Is_payed=False)
    return render(request, 'casher_dash/lab_payments.html', {'payments': payments ,'request_count': request_count})
# views for paying the lab payment for each patient
def checked_payment_request(request, patient_id):
    pay_request = get_object_or_404(Laboratory, PatientID=patient_id)
    pay_request.Is_payed = True
    pay_request.save()
    messages.success(request, 'lab. payment request is  payed successfully.')
    request_count = cache.get('request_count', 0)
    request_count -= 1
    cache.set('request_count', request_count)
    return redirect('check_payment_request')
# view for tadding prescriptions 
def add_perscription(request):
    users=User.objects.all()
    registered=False
    if request.method == 'POST':
        patientid = request.POST.get('patient_id')
        prec_number = request.POST.get('pec_no')
        prec_date = request.POST.get('pres_date')
        p_name = request.POST.get('name')
        doctor_name = request.POST.get('dr_name')
        prec = request.POST.get('prescription')
        # Create an instance of Appointment model and save it
        try:
            patient = get_object_or_404( PatientRegister,patient_id=patientid)
            doctor = get_object_or_404(User, username=doctor_name)
            presc = Prescription(
                PatientID=patient,
                Prec_date=prec_date,
                Prec_number=prec_number,
                Doctor_ID=doctor,
                Patient_full_name=p_name,
                Precscriptions=prec,

                # Assign values to other fields similarly
            )
            presc.save()
            registered=True
        except PatientRegister.DoesNotExist:
            # Handle the case where the patient is not found
            # You can add appropriate error handling or redirect to an error page
            pass
        except UserProfileInfo2.DoesNotExist:
            # Handle the case where the doctor is not found
            # You can add appropriate error handling or redirect to an error page
            pass
        # return redirect('add-appointment') 
        return render(request,'doctor/add-perscription.html',{'register':registered})
    return render(request,'doctor/add-perscription.html',{'users':users})
def edit_perscription(request):
    return render(request,'doctor/edit-perscription.html')
def perscription(request):
    prescription= Prescription.objects.all()
    return render(request,'doctor/perscriptions.html',{'prescriptions':prescription})
def about_perscription(request):
    return render(request,'doctor/about-percription.html')

def dis_dr_dash_content(request):
    return render(request,'doctor/dash_content.html')

def edit_appointment(request):
    return render(request,'doctor/edit-appointment.html')
def dis_appointment(request):
    appointment=Appointment.objects.all()
    return render(request,'doctor/appointments.html',{'appointment':appointment})
def about_appointment(request):
    return render(request,'doctor/about-appointment.html')
def dis_history(request):
    histories = PatientHistory.objects.all()
    return render(request,'doctor/histories.html',{'histories':histories})
def add_history(request):
    users= User.objects.all()
    added_history=False
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        date = request.POST.get('date')
        syptoms = request.POST.get('symptom')
        disease = request.POST.get('disease')
        doctor_name = request.POST.get('dr_name')
        nurse_name = request.POST.get('nr_name')
 
        # Create an instance of Appointment model and save it
        try:
            patient = get_object_or_404( PatientRegister,patient_id=patient_id)
            doctor = get_object_or_404(User, username=doctor_name)
            nurse = get_object_or_404(User, username=nurse_name)
            history = PatientHistory(
                Patient_ID=patient,
                Sympthom=syptoms,
                Date=date,
                Doctor_ID=doctor,
                DiseaseName=disease,
                Nurse_ID = nurse

                # Assign values to other fields similarly
            )
            history.save()
            added_history=True
        except PatientRegister.DoesNotExist:
            # Handle the case where the patient is not found
            # You can add appropriate error handling or redirect to an error page
            pass
        except UserProfileInfo2.DoesNotExist:
            # Handle the case where the doctor is not found
            # You can add appropriate error handling or redirect to an error page
            pass
        # return redirect('add-appointment') 
        return render(request,'doctor/add_history.html',{'added_history':added_history,'users':users})
    return render(request,'doctor/add_history.html',{'users':users})

def edit_history(request,history_no):
    users= User.objects.all()
    editing_history=False
    history = PatientHistory.objects.get(pk=history_no)
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        date = request.POST.get('date')
        syptoms = request.POST.get('symptom')
        disease = request.POST.get('disease')
        doctor_name = request.POST.get('dr_name')
        nurse_name = request.POST.get('nr_name')
 
        # Create an instance of Appointment model and save it
        try:
            doctor = get_object_or_404(User, username=doctor_name)
            nurse = get_object_or_404(User, username=nurse_name)
           
            history.Patient_ID=patient_id
            history.Sympthom=syptoms
            history.DiseaseName=disease
            history.Nurse_ID=nurse
            history.Doctor_ID=doctor
            history.Date=date
            history.save()
            editing_history=True
        except PatientRegister.DoesNotExist:
            # Handle the case where the patient is not found
            # You can add appropriate error handling or redirect to an error page
            pass
        except UserProfileInfo2.DoesNotExist:
            # Handle the case where the doctor is not found
            # You can add appropriate error handling or redirect to an error page
            pass
        # return redirect('add-appointment') 
        return render(request,'doctor/edit_history.html',{'editing_history':editing_history,'users':users})
    return render(request,'doctor/edit_history.html',{'users':users,'history':history})

def create_appointment(request):
    user=User.objects.all()
    registered=False
    if request.method == 'POST':
        patientid = request.POST.get('patient_id')
        app_number = request.POST.get('app_no')
        app_date = request.POST.get('app_date')
        time_slot = request.POST.get('time_slot')
        doctor_name = request.POST.get('dr_name')
        app_reseon = request.POST.get('problem')
        app_status = request.POST.get('app_status')
     
        # Extract other fields similarly
        try:
        # Create an instance of Appointment model and save it
            patient = get_object_or_404( PatientRegister,patient_id=patientid)
            doctor = get_object_or_404(User, username=doctor_name)
            appointment = Appointment(
                PatientID=patient,
                App_number=app_number,
                App_date=app_date,
                Time_slot=time_slot,
                Doctor_ID=doctor,
                App_reseon=app_reseon,
                App_status=app_status,

                # Assign values to other fields similarly
            )
            appointment.save()
            registered=True
        except PatientRegister.DoesNotExist:
            # Handle the case where the patient is not found
            # You can add appropriate error handling or redirect to an error page
            pass
        except UserProfileInfo2.DoesNotExist:
            # Handle the case where the doctor is not found
            # You can add appropriate error handling or redirect to an error page
            pass
        return render(request, 'doctor/add-appointment.html',{'registered':registered}) # Redirect to a success page or another URL

    return render(request, 'doctor/add-appointment.html',{'users':user})

