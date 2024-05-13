
from django.shortcuts import render
from .models import  Appointment,Prescription,Laboratory,PatientHistory
from receptionist_app.models import PatientRegister
from django.shortcuts import get_object_or_404
from admin_app.models import UserProfileInfo,Notification
from django.core.cache import cache
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from HMS_project import settings
from twilio.rest import Client
from django.http import HttpResponse
from datetime import datetime, timedelta
from twilio.base.exceptions import TwilioRestException

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
    unseen_count = Notification.objects.filter(Seen=False).count()
    return render(request, 'doctor/profile_show.html', {'user': user,'notifications':notifications,
                                                        'unseen_count':unseen_count})

@login_required
def profile_update_doc(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.user != user:  # Ensure user can only update their own profile
        return redirect('show_doctor_profile')
    
    user_profile, created = UserProfileInfo.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        user_profile.profile_pic = profile_pic
        user_profile.save()
        return redirect('show_doctor_profile')
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    return render(request, 'doctor/update_profile.html', {'user_id': user_id,
                                                           'user_profile': user_profile,
                                                           'notifications':notifications,
                                                        'unseen_count':unseen_count})

# @login_required
def dis_dr_dash(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    appointment=Appointment.objects.all()
    app_count=Appointment.objects.filter(App_status='Pending').count()
    patient_count=PatientRegister.objects.filter(is_checked=False,is_card=True).count()
    lab_requests = Laboratory.objects.filter(Is_tested=True,Is_prescriped=False,Is_payed=True).count()
    return render(request,'doctor/dr_dash.html',{
                                                'app_count':app_count,
                                                'patient_count':patient_count,
                                                'lab_requests':lab_requests,
                                                'notifications':notifications,
                                                'unseen_count':unseen_count,
                                                'appointments':appointment})
@login_required
def dis_labtest(request):
    labs= Laboratory.objects.all()
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    return render(request,'doctor/labtests.html',{'labs':labs,'notifications':notifications,
                                                'unseen_count':unseen_count})
@login_required
def add_lab(request):
    doctors = User.objects.filter(userprofileinfo__role='doctor')
    techs = User.objects.filter(userprofileinfo__role='technician')
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
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
        except Http404:
            messages.error(request, 'Users Does not exist!!')
            return render(request, 'doctor/add_lab.html')
        return render(request,'doctor/add_lab.html',{'register':registered,'notifications':notifications,
                                               'unseen_count':unseen_count,
                                               'technicians_with_test_counts':technicians_with_test_counts})
    
    return render(request,'doctor/add_lab.html',{'doctors':doctors,'techs':techs,'notifications':notifications,
                                                'unseen_count':unseen_count,
                                                'technicians_with_test_counts':technicians_with_test_counts})
# views for getting untested lab request and render it
@login_required
def check_request(request):
    request_count = cache.get('request_count', 0)
    requests = Laboratory.objects.filter(Is_tested=False)
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
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
    paginator = Paginator(payments, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'casher_dash/lab_payments.html', {'page_obj': page_obj ,'request_count': request_count})
# views for paying the lab payment for each patient
@login_required
def checked_payment_request(request, lab_number):
    pay_request = get_object_or_404(Laboratory, Lab_number=lab_number)
    pay_request.Is_payed = True
    pay_request.save()
    messages.success(request, 'lab. payment request is  payed successfully.')
    request_count = cache.get('request_count', 0)
    request_count -= 1
    cache.set('request_count', request_count)
    return redirect('check_payment_request')
# view for tadding prescriptions 
@login_required
def add_perscription(request,lab_number):
    labs = get_object_or_404( Laboratory,Lab_number=lab_number)
    patient_names = get_object_or_404( PatientRegister,patient_id=labs.PatientID)
    doctors = User.objects.filter(userprofileinfo__role='doctor')
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    registered=False
    if request.method == 'POST':
        patientid = request.POST.get('patient_id')
        p_name = request.POST.get('name')
        doctor_name = request.POST.get('dr_name')
        prec = request.POST.get('prescription')
        # Create an instance of Appointment model and save it
        try:
            patient = get_object_or_404( PatientRegister,patient_id=patientid)
            doctor = get_object_or_404(User, username=doctor_name)
            presc = Prescription(
                PatientID=patient,
                Doctor_ID=doctor,
                Patient_full_name=p_name,
                Precscriptions=prec,

                # Assign values to other fields similarly
            )
            presc.save()
            labs.Is_prescriped=True
            labs.save()
            registered=True
            return redirect('dis_lab_results')
        except Http404:
            messages.error(request, 'Users Does not exist!!')
            return render(request,'doctor/add-perscription.html',{'doctors':doctors,
                                                          'notifications':notifications,
                                                          'labs':labs,
                                                          'patient_names':patient_names.first_name + ' ' + patient_names.middle_name,
                                                'unseen_count':unseen_count}) 
        
    return render(request,'doctor/add-perscription.html',{'doctors':doctors,
                                                          'notifications':notifications,
                                                          'labs':labs,
                                                          'patient_names':patient_names.first_name + ' ' + patient_names.middle_name,
                                                'unseen_count':unseen_count})
@login_required
def add_perscription_second(request):
    doctors = User.objects.filter(userprofileinfo__role='doctor')
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    registered=False
    if request.method == 'POST':
        patientid = request.POST.get('patient_id')
        p_name = request.POST.get('name')
        doctor_name = request.POST.get('dr_name')
        prec = request.POST.get('prescription')
        # Create an instance of Appointment model and save it
        try:
            patient = get_object_or_404( PatientRegister,patient_id=patientid)
            doctor = get_object_or_404(User, username=doctor_name)
            presc = Prescription(
                PatientID=patient,
                Doctor_ID=doctor,
                Patient_full_name=p_name,
                Precscriptions=prec,

                # Assign values to other fields similarly
            )
            presc.save()
            registered=True
            return redirect('perscriptions')
        except Http404:
            messages.error(request, 'Users Does not exist!!')
            return render(request,'doctor/add_prescr_second.html',{'doctors':doctors,
                                                          'notifications':notifications,
                                                          'registered':registered,
                                                'unseen_count':unseen_count}) 
        
    return render(request,'doctor/add_prescr_second.html',{'doctors':doctors,
                                                          'notifications':notifications,
                                                          'registered':registered,
                                                'unseen_count':unseen_count})
@login_required

def edit_perscription(request, prec_number):
    users = User.objects.all()
    prescription = get_object_or_404(Prescription, Prec_number=prec_number)
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()

    if request.method == 'POST':
        patientid = request.POST.get('patient_id')
        p_name = request.POST.get('name')
        doctor_name = request.POST.get('dr_name')
        prec = request.POST.get('prescription')
        
        try:
            patient = get_object_or_404(PatientRegister, patient_id=patientid)
            doctor = get_object_or_404(User, username=doctor_name)

            prescription.PatientID = patient
            prescription.Doctor_ID = doctor
            prescription.Patient_full_name = p_name
            prescription.Precscriptions = prec
            prescription.save()
            return redirect('perscriptions')
        except Http404:
            messages.error(request, 'Users Does not exist!!')
            return render(request, 'doctor/edit-perscription.html', {
            'users': users,
            'notifications': notifications,
            'unseen_count': unseen_count,
            'prescriptions': prescription  # Pass prescription as a list for rendering
        })

    return render(request, 'doctor/edit-perscription.html', {
        'users': users,
        'notifications': notifications,
        'unseen_count': unseen_count,
        'prescriptions': prescription  # Pass prescription as a list for rendering
    })

@login_required
def perscription(request):
    prescription= Prescription.objects.all()
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    
    return render(request,'doctor/perscriptions.html',{'prescriptions':prescription,'notifications':notifications,
                                                'unseen_count':unseen_count})
def about_perscription(request,prec_number, patient_id):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    patient_info = get_object_or_404( PatientRegister,patient_id=patient_id)
    prec = get_object_or_404(Prescription, Prec_number=prec_number)
    return render(request,'doctor/about-percription.html',{'patient_info':patient_info,
                                                           'priscriptions':prec,
                                                           'notifications':notifications,
                                                           'unseen_count':unseen_count})
@login_required
def dis_dr_dash_content(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    appointment=Appointment.objects.all()
    app_count=Appointment.objects.filter(App_status='Pending').count()
    patient_count=PatientRegister.objects.filter(is_checked=False,is_card=True).count()
    lab_requests = Laboratory.objects.filter(Is_tested=True,Is_prescriped=False,Is_payed=True).count()
    return render(request,'doctor/dash_content.html',{'notifications':notifications,
                                                'app_count':app_count,
                                                'patient_count':patient_count,
                                                'lab_requests':lab_requests,
                                                'unseen_count':unseen_count,
                                                'appointments':appointment})
from datetime import datetime

@login_required
def edit_appointment(request, app_number):
    doctors = User.objects.filter(userprofileinfo__role='doctor')
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    appointments = Appointment.objects.get(App_number=app_number)
    
    start_time_parsed = None
    end_time_parsed = None
    
    if request.method == 'POST':
        patientid = request.POST.get('patient_id')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        doctor_name = request.POST.get('dr_name')
        app_reseon = request.POST.get('problem')
        app_date = request.POST.get('app_date')
        app_status = request.POST.get('app_status')
        patient = get_object_or_404(PatientRegister, patient_id=patientid)
        doctor = get_object_or_404(User, username=doctor_name)
        
        try:
            start_time_parsed = datetime.strptime(start_time, '%I:%M %p').time()
            end_time_parsed = datetime.strptime(end_time, '%I:%M %p').time()
            app_date_parsed = datetime.strptime(app_date, '%B %d, %Y').date()
            appointments.PatientID = patient
            appointments.Time_slot = start_time_parsed
            appointments.Time_slot = end_time_parsed
            appointments.Appointment_date = app_date_parsed
            appointments.App_reseon = app_reseon
            appointments.Doctor_ID = doctor
            appointments.App_status = app_status
            appointments.save()
            return redirect('dis-appointment')
        except Http404:
            messages.error(request, 'Users or Patient Does not exist!!')
            return render(request, 'doctor/edit-appointment.html', {'notifications': notifications,
                                                             'unseen_count': unseen_count,
                                                             'doctors': doctors,
                                                             'appointments': appointments})
    
    return render(request, 'doctor/edit-appointment.html', {'notifications': notifications,
                                                             'unseen_count': unseen_count,
                                                             'doctors': doctors,
                                                             'appointments': appointments})

@login_required
def dis_appointment(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    appointment=Appointment.objects.all()
    return render(request,'doctor/appointments.html',{'appointment':appointment,'notifications':notifications,
                                                'unseen_count':unseen_count})
def about_appointment(request,app_number):
    app = get_object_or_404(Appointment, App_number=app_number)
    return render(request,'doctor/about-appointment.html',{'appointemts':app})

def edit_lab_test(request, lab_number):
    doctors = User.objects.filter(userprofileinfo__role='doctor')
    techs = User.objects.filter(userprofileinfo__role='technician')
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()

    lab = get_object_or_404(Laboratory, Lab_number=lab_number)

    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
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

        try:
            patient = get_object_or_404(PatientRegister, patient_id=patient_id)
            doctor = get_object_or_404(User, username=doctor_name)
            technic = get_object_or_404(User, username=techn_name)
        
            lab.PatientID = patient
            lab.Doctor_ID = doctor
            lab.Technician_ID = technic
            lab.Lab_type = lab_type
            lab.save()

            return redirect('lab_tests')  # Redirect to lab tests page after successful update
        except Http404:
            messages.error(request, 'Users or Patient Does not exist!!')
            return render(request, 'doctor/edit_lab_test.html', {
        'labs': lab,
        'notifications': notifications,
        'unseen_count': unseen_count,
        'doctors': doctors,
        'techs': techs
    })

    return render(request, 'doctor/edit_lab_test.html', {
        'labs': lab,
        'notifications': notifications,
        'unseen_count': unseen_count,
        'doctors': doctors,
        'techs': techs
    })

def test_notification(request):
    return render(request,'doctor/view_notification.html')
@login_required
def dis_history(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    histories = PatientHistory.objects.all()
    return render(request,'doctor/histories.html',{'histories':histories,'notifications':notifications,
                                                'unseen_count':unseen_count})
@login_required
def dis_lab_results(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    lab_results = Laboratory.objects.filter(Is_tested=True, Is_payed=True,Is_prescriped=False)
    return render(request,'doctor/lab_results.html',{'lab_results':lab_results,'notifications':notifications,
                                                'unseen_count':unseen_count})
@login_required
def add_history(request, patient_id):
    patients = get_object_or_404(PatientRegister, patient_id=patient_id)
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    doctors = User.objects.filter(userprofileinfo__role='doctor')
    nurses = User.objects.filter(userprofileinfo__role='nurse')
    added_history = False
    if request.method == 'POST':
        patientid = request.POST.get('patient_id')
        syptom = request.POST.get('symptom')
        detailsyptoms = request.POST.get('detailsymptom')
        disease = request.POST.get('disease')
        doctor_name = request.POST.get('dr_name')
        nurse_name = request.POST.get('nr_name')
        
        try:
            patient = get_object_or_404(PatientRegister, patient_id=patientid)
            doctor = get_object_or_404(User, username=doctor_name)
            
            history = PatientHistory(
                Patient_ID=patient,
                symptom2=syptom,
                Sympthom=detailsyptoms,
                Doctor_ID=doctor,
                DiseaseName=disease,
                Nurse_ID=nurse_name
            )
            history.save()
            patients.is_checked = True
            patients.save()
            messages.success(request, 'Patient is checked successfully.')

            patient_count = cache.get('patient_count', 0)
            patient_count -= 1
            cache.set('patient_count', patient_count)
            return redirect('check_patient_data')
        except Http404:
            messages.error(request, 'Users or Patient Does not exist!!')
            return render(request, 'doctor/add_history.html', {'doctors': doctors, 'nurses': nurses, 'notifications': notifications,
                                                       'unseen_count': unseen_count, 'patients': patients})
    return render(request, 'doctor/add_history.html', {'doctors': doctors, 'nurses': nurses, 'notifications': notifications,
                                                       'unseen_count': unseen_count, 'patients': patients})

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
        try:
            history.Patient_ID= patient
            history.Sympthom = symptoms
            history.DiseaseName = disease
            history.Nurse_ID= nurse
            history.Doctor_ID = doctor
            history.Date = date
            history.save()
            return redirect('dis_history')  # Redirect to a success URL
        except Http404:
            messages.error(request, 'Users or Patient Does not exist!!')
            return redirect('dis_history') 
  

@login_required
def edit_history(request, history_no):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    doctors = User.objects.filter(userprofileinfo__role='doctor')
    nurses = User.objects.filter(userprofileinfo__role='nurse')
   
    try:
        
        history1 = get_object_or_404(PatientHistory, pk=history_no)
        return render(request, 'doctor/edit_history.html', {
    
        'doctors': doctors,
        'nurses': nurses,
        'history': history1,
        'notifications': notifications,
        'unseen_count': unseen_count
    })  # Redirect to a success URL
    except Http404:
            messages.error(request, 'Users or Patient Does not exist!!')
            return render(request,'doctor/histories.html')
       


@login_required
def create_appointment(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    doctors = User.objects.filter(userprofileinfo__role='doctor')
    registered=False
    if request.method == 'POST':
        patientid = request.POST.get('patient_id')
        start_time= request.POST.get('start_time')
        end_time= request.POST.get('end_time')
        doctor_name = request.POST.get('dr_name')
        app_reseon = request.POST.get('problem')
        app_date = request.POST.get('app_date')
        app_status = request.POST.get('app_status')
        
        # Extract other fields similarly
        try:
        # Create an instance of Appointment model and save it
            patient = get_object_or_404( PatientRegister,patient_id=patientid)
            doctor = get_object_or_404(User, username=doctor_name)
            uemail= patient.email
            phone_number=patient.phone_number
            appointment = Appointment(
                PatientID=patient,
                Start_Time=start_time,
                End_Time=end_time,
                Appointment_date=app_date,
                Doctor_ID=doctor,
                App_reason=app_reseon,
                App_status=app_status,

                # Assign values to other fields similarly
            )
            registered=True
            appointment.save()
        except Http404:
            messages.error(request, 'Users or Patient Does not exist!!')
            return render(request, 'doctor/add-appointment.html',{'doctors':doctors,'notifications':notifications,
                                                'unseen_count':unseen_count})
            
        context = {
            'first_name':patient.first_name,
            'middle_name':patient.middle_name,
            'timeslot':start_time
        }
        html_message = render_to_string('doctor/email_templates.html', context)
        plain_message = strip_tags(html_message)
        send_mail(
            'Account Created',
            plain_message,
            settings.EMAIL_HOST_USER,
            [uemail],
            html_message=html_message,
            fail_silently=False,
        )
        

        if phone_number.startswith('0'):
            phone_number = '+251' + phone_number[1:]

        # Twilio credentials
        account_sid = 'ACfa34a64a48ac610545ce9cee8c70bb15'
        auth_token = 'a4c42e61f3487ad86f7bea242dbacb07'
        twilio_number = '+14844984613'

        # Initialize Twilio client
        client = Client(account_sid, auth_token)
        app_notify = 'Hello! ' + patient.first_name  + '\nAppointment Day: '+ app_date + '\nAt time: '+ start_time
        try:
            # Send SMS
            message = client.messages.create(
                body=app_notify,
                from_=twilio_number,
                to=phone_number
            )

            # Save sent message to database
            return redirect('add-appointment')
        except TwilioRestException as e:
            error_message = f'Twilio Error: {e.msg}'
        return render(request, 'doctor/add-appointment.html',{'registered':registered,'notifications':notifications,
                                                'unseen_count':unseen_count}) # Redirect to a success page or another URL

    return render(request, 'doctor/add-appointment.html',{'doctors':doctors,'notifications':notifications,
                                                'unseen_count':unseen_count})

