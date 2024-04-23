
from django.shortcuts import render
from .models import  Appointment,Prescription,Laboratory,PatientHistory
from receptionist_app.models import PatientRegister
from django.shortcuts import get_object_or_404
from admin_app.models import UserProfileInfo2,Notification
from django.core.cache import cache
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def technician_list(request):
    # Get all distinct technician IDs from the Laboratory model
    technician_ids = Laboratory.objects.values_list('Technician_ID', flat=True).distinct()

    technicians_with_test_counts = []
    for technician_id in technician_ids:
        # Get the technician user object using the technician ID
        technician = User.objects.get(pk=technician_id)

        # Count the number of untested laboratory tests assigned to the technician
        untested_test_count = Laboratory.objects.filter(Technician_ID=technician_id, Is_tested=False).count()

        # If there are no untested tests, set the test count to 0
        test_count = untested_test_count if untested_test_count > 0 else 0

        technicians_with_test_counts.append((technician, test_count))
    
    return render(request, 'doctor/technician_list.html', {'technicians_with_test_counts': technicians_with_test_counts})
@login_required
def doc_profile(request):
    user = request.user
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request, 'doctor/profile_show.html', {'user': user,'notifications':notifications,
                                                        'unseen_count':unseen_count})

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
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request, 'doctor/update_profile.html', {'user_id': user_id,
                                                           'user_profile': user_profile,
                                                           'notifications':notifications,
                                                        'unseen_count':unseen_count})

@login_required
def dis_dr_dash(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request,'doctor/dr_dash.html',{
                                                'notifications':notifications,
                                                'unseen_count':unseen_count})
@login_required
def dis_labtest(request):
    labs= Laboratory.objects.all()
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request,'doctor/labtests.html',{'labs':labs,'notifications':notifications,
                                                'unseen_count':unseen_count})
@login_required
def add_lab(request):
    users=User.objects.all()
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    registered=False
    technician_ids = Laboratory.objects.values_list('Technician_ID', flat=True).distinct()

    technicians_with_test_counts = []
    for technician_id in technician_ids:
        # Get the technician user object using the technician ID
        technician = User.objects.get(pk=technician_id)

        # Count the number of untested laboratory tests assigned to the technician
        untested_test_count = Laboratory.objects.filter(Technician_ID=technician_id, Is_tested=False).count()

        # If there are no untested tests, set the test count to 0
        test_count = untested_test_count if untested_test_count > 0 else 0

        technicians_with_test_counts.append((technician, test_count))
    if request.method == 'POST':
        patientid = request.POST.get('patient_id')
        lab_number = request.POST.get('lab_no')
        admit_date = request.POST.get('admited_date')
        doctor_name = request.POST.get('dr_name')
        techn_name = request.POST.get('techn_name')
        checkbox1 = request.POST.get('blood_test') == 'on'
        checkbox2 = request.POST.get('urine_test') == 'on'
        checkbox3 = request.POST.get('ctscan_test') == 'on'
        checkbox4 = request.POST.get('x-ray_test') == 'on'
        lab_type = ''

        if checkbox1:
            lab_type += 'Blood '
        if checkbox2:
            lab_type += 'Urine '
        if checkbox3:
            lab_type += 'CT Scan '
        if checkbox4:
            lab_type += 'X-ray '

# Remove the trailing space if lab_type is not empty
        lab_type = lab_type.strip() if lab_type else None
        # Create an instance of Appointment model and save it
        try:
            patient = get_object_or_404( PatientRegister,patient_id=patientid)
            doctor = get_object_or_404(User, username=doctor_name)
            technic = get_object_or_404(User, username=techn_name)
            lab = Laboratory(
                PatientID=patient,
                Admit_date=admit_date,
                Lab_number=lab_number,
                Doctor_ID=doctor,
                Technician_ID=technic,
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
        return render(request,'doctor/add_lab.html',{'register':registered,'notifications':notifications,
                                               'unseen_count':unseen_count,
                                               'technicians_with_test_counts':technicians_with_test_counts})
    
    return render(request,'doctor/add_lab.html',{'users':users,'notifications':notifications,
                                                'unseen_count':unseen_count,
                                                'technicians_with_test_counts':technicians_with_test_counts})
# views for getting untested lab request and render it
@login_required
def check_request(request):
    request_count = cache.get('request_count', 0)
    requests = Laboratory.objects.filter(Is_tested=False)
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request, 'laboratory_dash/lab_requests.html', {'requests': requests ,
                                                                 'request_count': request_count,
                                                                 'notifications':notifications,
                                                'unseen_count':unseen_count})
# views for testing the lab for single patient 
@login_required
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
@login_required
def check_payment_request(request):
    request_count = cache.get('request_count', 0)
    payments = Laboratory.objects.filter(Is_payed=False)
    return render(request, 'casher_dash/lab_payments.html', {'payments': payments ,'request_count': request_count})
# views for paying the lab payment for each patient
@login_required
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
@login_required
def add_perscription(request):
    users=User.objects.all()
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
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
        return render(request,'doctor/add-perscription.html',{'register':registered,
                                                              'notifications':notifications,
                                                'unseen_count':unseen_count,
                                                'users':users})
    return render(request,'doctor/add-perscription.html',{'users':users,'notifications':notifications,
                                                'unseen_count':unseen_count})
@login_required
def edit_perscription(request,prec_number):
    users=User.objects.all()
    prescription= Prescription.objects.get(Prec_number=prec_number)
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    if request.method == 'POST':
        patientid = request.POST.get('patient_id')
        prec_no = request.POST.get('pec_no')
        prec_date = request.POST.get('pres_date')
        p_name = request.POST.get('name')
        doctor_name = request.POST.get('dr_name')
        prec = request.POST.get('prescription')
        # Create an instance of Prescription model and save it
        try:
            patient = get_object_or_404( PatientRegister,patient_id=patientid)
            doctor = get_object_or_404(User, username=doctor_name)
        
            prescription.PatientID=patient
            prescription.Prec_date=prec_date
            prescription.Prec_number=prec_no
            prescription.Doctor_ID=doctor
            prescription.Patient_full_name=p_name
            prescription.Precscriptions=prec
            prescription.save()
            
        except PatientRegister.DoesNotExist:
            pass
        except UserProfileInfo2.DoesNotExist:
            pass
        return redirect('perscriptions')
    return render(request,'doctor/edit-perscription.html',{'users':users,'notifications':notifications,
                                                'unseen_count':unseen_count,
                                                'prescriptions':prescription})
@login_required
def perscription(request):
    prescription= Prescription.objects.all()
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    
    return render(request,'doctor/perscriptions.html',{'prescriptions':prescription,'notifications':notifications,
                                                'unseen_count':unseen_count})
def about_perscription(request,prec_number, patient_id):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    patient_info = get_object_or_404( PatientRegister,patient_id=patient_id)
    prec = get_object_or_404(Prescription, Prec_number=prec_number)
    return render(request,'doctor/about-percription.html',{'patient_info':patient_info,
                                                           'priscriptions':prec,
                                                           'notifications':notifications,
                                                           'unseen_count':unseen_count})
@login_required
def dis_dr_dash_content(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request,'doctor/dash_content.html',{'notifications':notifications,
                                                'unseen_count':unseen_count})
@login_required
def edit_appointment(request,app_number):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    appointments = Appointment.objects.get(App_number=app_number)
    if request.method == 'POST': 

        patientid = request.POST.get('patient_id')
        app_no = request.POST.get('app_no')
        app_date = request.POST.get('app_date')
        time_slot = request.POST.get('time_slot')
        doctor_name = request.POST.get('dr_name')
        app_reseon = request.POST.get('problem')
        app_status = request.POST.get('app_status')
        patient = get_object_or_404( PatientRegister,patient_id=patientid)
        doctor = get_object_or_404(User, username=doctor_name)
        
        appointments.App_number =app_no
        appointments.PatientID =patient
        appointments.App_date =app_date
        appointments.Time_slot =time_slot
        appointments.App_reseon =app_reseon
        appointments.Doctor_ID =doctor
        appointments.App_status =app_status
        appointments.save()
        return redirect('dis-appointment')
    return render(request,'doctor/edit-appointment.html',{'notifications':notifications,
                                                'unseen_count':unseen_count,
                                                'appointments':appointments})
@login_required
def dis_appointment(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    appointment=Appointment.objects.all()
    return render(request,'doctor/appointments.html',{'appointment':appointment,'notifications':notifications,
                                                'unseen_count':unseen_count})
def about_appointment(request):
    return render(request,'doctor/about-appointment.html')
def test_notification(request):
    return render(request,'doctor/view_notification.html')
@login_required
def dis_history(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    histories = PatientHistory.objects.all()
    return render(request,'doctor/histories.html',{'histories':histories,'notifications':notifications,
                                                'unseen_count':unseen_count})
@login_required
def dis_lab_results(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    lab_results = Laboratory.objects.filter(Is_tested=True, Is_payed=True)
    return render(request,'doctor/lab_results.html',{'lab_results':lab_results,'notifications':notifications,
                                                'unseen_count':unseen_count})
@login_required
def add_history(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
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
        return render(request,'doctor/add_history.html',{'added_history':added_history,'users':users,'notifications':notifications,
                                                'unseen_count':unseen_count})
    return render(request,'doctor/add_history.html',{'users':users,'notifications':notifications,
                                                'unseen_count':unseen_count})
@login_required
def update_history(request, history_no):
        patient_id = request.POST.get('patient_id')
        date = request.POST.get('date')
        symptoms = request.POST.get('symptom')
        disease = request.POST.get('disease')
        doctor_name = request.POST.get('dr_name')
        nurse_name = request.POST.get('nr_name')
        history = PatientHistory.objects.get(pk=history_no)  
        doctor = get_object_or_404(User, username=doctor_name)
        nurse = get_object_or_404(User, username=nurse_name)
        patient = get_object_or_404( PatientRegister,patient_id=patient_id)

        history.Patient_ID= patient
        history.Sympthom = symptoms
        history.DiseaseName = disease
        history.Nurse_ID= nurse
        history.Doctor_ID = doctor
        history.Date = date
        history.save()
        return redirect('dis_history')  # Redirect to a success URL
  

@login_required
def edit_history(request, history_no):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    users = User.objects.all()
   
    try:
        
        history1 = get_object_or_404(PatientHistory, pk=history_no)
        return render(request, 'doctor/edit_history.html', {
    
        'users': users,
        'history': history1,
        'notifications': notifications,
        'unseen_count': unseen_count
    })  # Redirect to a success URL
    except PatientHistory.DoesNotExist:
            # Handle the case where the user (doctor or nurse) is not found
            # You can add appropriate error handling or redirect to an error page
        return redirect('dis_history')
       


@login_required
def create_appointment(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
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
        return render(request, 'doctor/add-appointment.html',{'registered':registered,'notifications':notifications,
                                                'unseen_count':unseen_count}) # Redirect to a success page or another URL

    return render(request, 'doctor/add-appointment.html',{'users':user,'notifications':notifications,
                                                'unseen_count':unseen_count})

