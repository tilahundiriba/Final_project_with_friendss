
from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from django.contrib.auth import login
from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from HMS_project import settings
from .utils import generate_username, generate_password
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import UserProfileInfo
# from .models import PatientChange
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Notification
from receptionist_app.models import PatientRegister
from doctor_app.models import Appointment,PatientHistory,Laboratory,Prescription
from casher_app.models import PaymentModel,Discharge,ServicePayment
from nurse_app.models import RoomInformation,VitalInformation,Medication
import csv
import openpyxl
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table,TableStyle
from reportlab.lib import colors
from django.shortcuts import render, get_object_or_404
from .models import User, UserProfileInfo,Feedback,Report
from .models import Notification
from doctor_app.models import Laboratory

# views.py
from datetime import datetime
from django.shortcuts import render
from django.template.loader import render_to_string




def registration_years(request):
    # Get the current year
    current_year = datetime.now().year

    # Create a list of years from 2022 to the current year
    years = list(range(2022, current_year + 1))

    # Query the database to count registrations for each year
    registration_counts = [
        {
            'year': year,
            'count': Appointment.objects.filter(App_date__year=year).count()  # Replace YourModel and date_of_registration with your actual model and field names
        }
        for year in years
    ]
    context= {'registration_counts':registration_counts}
    return JsonResponse({'registration_years': registration_counts})

def delete_medication(request):
    if 'delete' in request.POST:
        # Handle deletion of selected employees
        med_delete = request.POST.getlist('med_delete')
        Medication.objects.filter(Med_no__in=med_delete).delete()
        # Redirect to a success page or back to the medications list
    return redirect('medications')

def delete_labratory(request):
    if 'delete' in request.POST:
        # Handle deletion of selected employees
        lab_delete = request.POST.getlist('lab_delete')
        Laboratory.objects.filter(Lab_number__in=lab_delete).delete()
        # Redirect to a success page or back to the medications list

    return redirect('laboratories')

def delete_patient(request):
    # Retrieve the medication object
    if 'delete' in request.POST:
        # Handle deletion of selected employees
        patientid = request.POST.getlist('patient_delete')
        PatientRegister.objects.filter(patient_id__in=patientid).delete()
        # Redirect to a success page or back to the medications list
    return redirect('patient')  

def delete_vital(request):
    # Retrieve the medication object
    if 'delete' in request.POST:
        # Handle deletion of selected employees
        vital_no = request.POST.getlist('vital_delete')
        VitalInformation.objects.filter(Vital_info_no__in=vital_no).delete()
        # Redirect to a success page or back to the medications list
    return redirect('vitals') 

def delete_appointment(request):
    if 'delete' in request.POST:
        # Handle deletion of selected employees
        app_delete = request.POST.getlist('app_delete')
        Appointment.objects.filter(App_number__in=app_delete).delete()
        # Redirect to a success page or back to the medications list
        return redirect('dis_appointment') 

def delete_history(request):
    # Retrieve the medication object
    if 'delete' in request.POST:
        # Handle deletion of selected employees
        his_delete = request.POST.getlist('his_delete')
        PatientHistory.objects.filter(History_No__in=his_delete).delete()
        # Redirect to a success page or back to the medications list
    return redirect('history') 

def delete_prescription(request):
    if 'delete' in request.POST:
        # Handle deletion of selected employees
        pres_delete = request.POST.getlist('pres_delete')
        Prescription.objects.filter(Prec_number__in=pres_delete).delete()
        # Redirect to a success page or back to the medications list
    return redirect('dis_perscription')  
def delete_payment(request):
     # Retrieve the medication object
    if 'delete' in request.POST:
        # Handle deletion of selected employees
        pay_delete = request.POST.getlist('pay_delete')
        PaymentModel.objects.filter(Pay_number__in=pay_delete).delete()
        # Redirect to a success page or back to the medications list
    return redirect('payments')  

def delete_discharge(request):
    if 'delete' in request.POST:
        # Handle deletion of selected employees
        dis_delete = request.POST.getlist('dis_delete')
        Discharge.objects.filter(Discharge_no__in=dis_delete).delete()
        # Redirect to a success page or back to the medications list
    return redirect('departed') 

# @login_required
def dis_appointment(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    appointment=Appointment.objects.all()
    return render(request,'admin_dash/appointments.html',{'appointment':appointment,'notifications':notifications,
                                                'unseen_count':unseen_count})
# @login_required
def dis_history(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    histories = PatientHistory.objects.all()
    return render(request,'admin_dash/histories.html',{'histories':histories,'notifications':notifications,
                                                'unseen_count':unseen_count})
# @login_required
def perscription(request):
    prescription= Prescription.objects.all()
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    
    return render(request,'admin_dash/prescriptions.html',{'prescriptions':prescription,'notifications':notifications,
                                                'unseen_count':unseen_count})
def dis_vitals(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    vitals =VitalInformation.objects.all()
    return render(request,'admin_dash/vital_infos.html',{'vitals':vitals,'notifications':notifications,
                                                       'unseen_count':unseen_count})
def dis_patient(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    patients = PatientRegister.objects.all()
    return render(request,'admin_dash/patients.html', {'patients':patients
                                                              ,
                                                              'notifications':notifications,
                                                              'unseen_count':unseen_count})
def dis_lab_result(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    lab_results = Laboratory.objects.all()
    return render(request, 'admin_dash/laboratories.html',{'notifications':notifications,
                                                'unseen_count':unseen_count,
                                                'lab_results':lab_results})
def dis_payment(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    payments = PaymentModel.objects.all()
    return render(request,'admin_dash/payments.html',{'notifications':notifications,
                                                            'unseen_count':unseen_count,
                                                            'payments':payments})
def dis_discharge(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    discharges = Discharge.objects.all()
    context = []

    for discharge in discharges:
        recent_payment = PaymentModel.objects.filter(Patient_id=discharge.Patient_id).order_by('-Admit_date').first()
        context.append({
            'patient_id': discharge.Patient_id,
            'no_days': discharge.No_days,
            'reason': discharge.Reason,
            'Discharge_no': discharge.Discharge_no,
            'referred_to': discharge.Reffer_to,
            'departure_date': discharge.Departure_date,
            'food_payment': recent_payment.Food_payment if recent_payment else None,
            'bed_payment': recent_payment.Bed_payment if recent_payment else None,
            # Add other fields from Discharge and PaymentModel as needed
        })
    return render(request,'admin_dash/departed.html',{'notifications':notifications,
                                                         'unseen_count':unseen_count,
                                                         'discharges':context})
def dis_medication(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    medications = Medication.objects.all()
    return render(request,'admin_dash/medications.html',{'medications':medications,
                                                            'notifications':notifications,
                                                       'unseen_count':unseen_count})
def add_report(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        document = request.FILES.get('report_file')
        names = get_object_or_404(User, username=name)
        report = Report(
            Name=names,
            Title=title,
            Report_file=document
        )
        report.save()

    return render(request, 'admin_dash/add_report.html')


# @login_required
def admin_profile(request):
    user = request.user
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    return render(request, 'admin_dash/admin_profile.html', {'user': user,'notifications':notifications,
                                                        'unseen_count':unseen_count})

# @login_required
def profile_update_admin(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.user != user:  # Ensure user can only update their own profile
        return redirect('admin_profile')
    
    user_profile, created = UserProfileInfo.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        user_profile.profile_pic = profile_pic
        user_profile.save()
        return redirect('admin_profile')
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    return render(request, 'doctor/update_profile.html', {'user_id': user_id,
                                                           'user_profile': user_profile,
                                                           'notifications':notifications,
                                                        'unseen_count':unseen_count})
def notification_view(request):
    # Fetch all notifications that haven't been seen by the user
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    return render(request, 'admin_dash/seeNotifications.html', {'notifications': notifications,'unseen_count': unseen_count})
def general_report(request):
    # Fetch all notifications that haven't been seen by the user
    current_time = datetime.now()  # Get the current system time

    context = {
        # Other context data
        'current_time': current_time # Pass the current time to the template
    }
    total_sum = PaymentModel.objects.aggregate(total_sum=Sum('Total'))['total_sum']
    total_sum = total_sum or 0
    number_of_payment = PaymentModel.objects.count()
    number_of_cash = PaymentModel.objects.filter(Pay_method='Cash').count()
    number_of_insurance= number_of_payment - number_of_cash
    cash_total_sums = PaymentModel.objects.filter(Pay_method='Cash').aggregate(total_sum=Sum('Total'))
    #cash_total_sum = cash_total_sums or 0
    cash_total_sum = cash_total_sums['total_sum'] or 0
    # Calculate total sum of payments for insurance
    insurance_total_sums = PaymentModel.objects.filter(Pay_method='Insurance').aggregate(total_sum=Sum('Total'))
    insurance_total_sum = insurance_total_sums['total_sum'] or 0
    #insurance_total_sum = insurance_total_sums or 0
    number_of_patient = PatientRegister.objects.count()
    number_of_app= Appointment.objects.count()
    number_of_bed= RoomInformation.objects.count()
    Occupied_of_bed= RoomInformation.objects.filter(Status='Occupied').count()
    free_bed = number_of_bed - Occupied_of_bed
    number_of_departure= Discharge.objects.count()
    patients_with_refere_to = Discharge.objects.exclude(Reffer_to='').count()
    patients_without_refere_to = number_of_departure - patients_with_refere_to
    number_of_cancelled= Appointment.objects.filter(App_status='Cancelled').count()
    number_of_pending= Appointment.objects.filter(App_status='Pending').count()
    number_of_completed= Appointment.objects.filter(App_status='Completed').count()
    number_of_history = PatientHistory.objects.count()
    checked_of_history = PatientHistory.objects.filter(Is_checked=True).count()
    uncheked_history = number_of_history - checked_of_history
    number_of_Presc= Prescription.objects.count()
    number_of_vitals= VitalInformation.objects.count()
    number_of_lab= Laboratory.objects.count()
    tested_of_lab= Laboratory.objects.filter(Is_tested=True).count()
    untested_lab = number_of_lab - tested_of_lab
    female_patient = PatientRegister.objects.filter(gender='female').count()
    male_patient = number_of_patient - female_patient
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    return render(request, 'admin_dash/general_report.html', 
                  {'notifications': notifications,
                    'unseen_count': unseen_count,
                    'number_of_patient': number_of_patient,
                    'female_patient': female_patient,
                    'male_patient': male_patient,
                    'number_of_departure': number_of_departure,
                    'patients_with_refere_to': patients_with_refere_to,
                    'patients_without_refere_to': patients_without_refere_to,
                    'number_of_history': number_of_history,
                    'checked_of_history': checked_of_history,
                    'uncheked_history': uncheked_history,
                    'number_of_Presc': number_of_Presc,
                    'number_of_lab': number_of_lab,
                    'tested_of_lab': tested_of_lab,
                    'untested_lab': untested_lab,
                    'number_of_app': number_of_app,
                    'number_of_cancelled': number_of_cancelled,
                    'number_of_pending': number_of_pending,
                    'number_of_completed': number_of_completed,
                    'number_of_bed': number_of_bed,
                    'Occupied_of_bed': Occupied_of_bed,
                    'free_bed': free_bed,
                    'total_sum': total_sum,
                    'number_of_cash': number_of_cash,
                    'cash_total_sum': cash_total_sum,
                    'number_of_insurance': number_of_insurance,
                    'insurance_total_sum': insurance_total_sum,
                    'number_of_vitals': number_of_vitals,
                    'number_of_payment': number_of_payment,
                    'context': context
                    })

def mark_notification_as_seen(request, id):
    # Get the notification by ID
    notification = Notification.objects.get(id=id)
    
    # Mark the notification as seen
    notification.Seen = True
    notification.save()
    if 'unseen_count' in request.session:
        request.session['unseen_count'] = max(0, request.session.get('unseen_count', 0) - 1)
    return redirect('index')

def poster(request):
    if request.method=='POST':
        message=request.POST.get('message')
        name=request.POST.get('name')
        title=request.POST.get('title')
        notification=Notification(
            Message=message,
            Name=name,
            Title=title
            )
        notification.save()
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    return render(request,'admin_dash/write-notifications.html',{'notifications':notifications,
                                                   'unseen_count':unseen_count})

# @login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # role = request.POST.get('role')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if user's profession matches
            try:
                user_profile = UserProfileInfo.objects.get(user=user)
                # if user_profile.role:
                login(request, user)
                if user_profile.password_changed:
                    if user_profile.role =='doctor':
                        return redirect('dis_dr_dash')  # Redirect to home URL after login
                    elif user_profile.role =='nurse':
                        return redirect('nurse_dash')
                    if user_profile.role =='admin':
                        return redirect('dis_dash')  # Redirect to home URL after login
                    elif user_profile.role =='casher':
                        return redirect('casher_dash')
                    elif user_profile.role =='receptionist':
                        return redirect('receptionist_dash')  # Redirect to home URL after login
                    elif user_profile.role =='technician':
                        return redirect('lab_dashboard')
                    else:
                        return redirect('patient_dash')
                else:
                    return redirect('change_credentials')
                # else:
                #     return HttpResponse('Invalid profession for the user')
            except UserProfileInfo.DoesNotExist:
                return HttpResponse('User does not have a role...!!!')

        else:
            # User authentication failed
            return HttpResponse('Invalid username or password')
    else:
        return render(request, 'admin_dash/login.html')
    # return render(request, 'admin_dash/login.html')

#@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('user_log'))
def approve_departure(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    unapproved = Discharge.objects.filter(Approval=False, Status='Completed', Reffer_to__isnull=False)
    return render(request,'admin_dash/discharge_approval.html',{'notifications':notifications,
                                                                'unseen_count':unseen_count,
                                                                'unapproved':unapproved})
def dis_service(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    services = ServicePayment.objects.all()
    return render(request,'admin_dash/services.html',{'notifications':notifications,
                                                                'unseen_count':unseen_count,
                                                                'services':services})
def add_service(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    if request.method=='POST':
        service_name=request.POST.get('service_name')
        service_cost=request.POST.get('scost')
        paye_method=request.POST.get('pmethod')
        notification=ServicePayment.objects.create(
            Services=service_name,
            Payment_method=paye_method,
            Payment=service_cost
            )
        return redirect('add_service')
    return render(request,'admin_dash/add-service.html',{'notifications':notifications,
                                                                'unseen_count':unseen_count
                                                                })
def edit_service(request,service):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    services = get_object_or_404(ServicePayment, Services=service)
    if request.method=='POST':
        service_name=request.POST.get('service_name')
        service_cost=request.POST.get('scost')
        paye_method=request.POST.get('pmethod')
        services.Services=service_name
        services.Payment_method=paye_method
        services.Payment=service_cost
        services.save()   
        return redirect('dis_service')
    return render(request,'admin_dash/edit-service.html',{'notifications':notifications,
                                                                'unseen_count':unseen_count,
                                                                'services':services
                                                                })
# @login_required
def createUserAccount(request):
    created=False
    if request.method == 'POST':
        email = request.POST.get('email')
        role = request.POST.get('role')
        special = request.POST.get('spec')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        # Generate username and password
        username = generate_username(email, role)
        password = generate_password()

        # Create the user
        hashed_password = make_password(password)
        user = User.objects.create_user(username=username,
                                        first_name=first_name,
                                        last_name=last_name ,
                                        email=email,
                                        password=password)

        # Create user profile
        user_profile = UserProfileInfo.objects.create(
            user=user,
            role=role,
            specialty=special
        )
        # Send email with username and password
        context = {
            'username': username,
            'password': password,
            'role': role,
            'speciality':special,
        }
        html_message = render_to_string('admin_dash/email_template.html', context)
        plain_message = strip_tags(html_message)
        send_mail(
            'Account Created',
            plain_message,
            settings.EMAIL_HOST_USER,
            [email],
            html_message=html_message,
            fail_silently=False,
        )
        created=True
        # Redirect to account list after account creation
        return render(request, 'admin_dash/add_staff.html',{'created':created})
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    return render(request, 'admin_dash/add_staff.html',{'notifications':notifications,
                                                   'unseen_count':unseen_count})
def dis_login2(request):
    return render(request,'admin_dash/login.html')
def dis_base(request):
    return render(request,'admin_app/base.html')
# admin dashboard views
# @login_required
def dis_dash(request):
    total_sum = PaymentModel.objects.aggregate(total_sum=Sum('Total'))['total_sum']
    total_sum = total_sum or 0
    number_of_patient = PatientRegister.objects.count()
    number_of_app= Appointment.objects.count()
    number_of_history = PatientHistory.objects.count()
    number_of_Presc= Prescription.objects.count()
    number_of_lab= Laboratory.objects.count()
    notifications = Notification.objects.all()

    unseen_count = Notification.objects.filter(Seen=False).count()
    unseen_feedbacks = Feedback.objects.filter(Is_seen=False)
    unseen_feedbacks_count = Feedback.objects.filter(Is_seen=False).count()
    cash_total_sums = PaymentModel.objects.filter(Pay_method='Cash').aggregate(total_sum=Sum('Total'))
    cash_total_sum = cash_total_sums['total_sum'] or 0
    insurance_total_sums = PaymentModel.objects.filter(Pay_method='Insurance').aggregate(total_sum=Sum('Total'))
    insurance_total_sum = insurance_total_sums['total_sum'] or 0
    number_of_cancelled= Appointment.objects.filter(App_status='Cancelled').count()
    number_of_pending= Appointment.objects.filter(App_status='Pending').count()
    number_of_completed= Appointment.objects.filter(App_status='Completed').count()
    return render(request,'admin_dash/dashboard.html',{'number_patients':number_of_patient,
                                                   'number_of_app':number_of_app,
                                                   'total_amount':total_sum,
                                                   'notifications':notifications,
                                                   'number_of_history':number_of_history,
                                                   'number_of_Presc':number_of_Presc,
                                                   'cash_total_sum':cash_total_sum,
                                                   'insurance_total_sum':insurance_total_sum,
                                                   'number_of_lab':number_of_lab,
                                                   'number_of_cancelled':number_of_cancelled,
                                                   'number_of_pending':number_of_pending,
                                                   'number_of_completed':number_of_completed,
                                                   'unseen_count':unseen_count,
                                                   'unseen_feedbacks':unseen_feedbacks,
                                                   'unseen_feedbacks_count':unseen_feedbacks_count
                                                   })
# @login_required
def dis_dash_content(request):
    cash_total_sums = PaymentModel.objects.filter(Pay_method='Cash').aggregate(total_sum=Sum('Total'))
    cash_total_sum = cash_total_sums['total_sum'] or 0
    insurance_total_sums = PaymentModel.objects.filter(Pay_method='Insurance').aggregate(total_sum=Sum('Total'))
    insurance_total_sum = insurance_total_sums['total_sum'] or 0
    unseen_feedbacks = Feedback.objects.filter(Is_seen=False)
    unseen_feedbacks_count = Feedback.objects.filter(Is_seen=False).count()
      # Get the current year
    current_year = datetime.now().year

    # Create a list of years from 2022 to the current year
    years = list(range(2022, current_year + 1))

    # Query the database to count registrations for each year
    registration_counts = [
        {
            'year': year,
            'count': Appointment.objects.filter(App_date__year=year).count()  # Replace YourModel and date_of_registration with your actual model and field names
        }
        for year in years
    ]
    context= {'registration_counts':registration_counts}
    return render(request,'admin_dash/dash_content.html',{'cash_total_sum':cash_total_sum,
                                                          'insurance_total_sum':insurance_total_sum,
                                                          'unseen_feedbacks':unseen_feedbacks,
                                                          'unseen_feedbacks_count':unseen_feedbacks_count,
                                                          'context':context})
# @login_required
def refere_info(request,discharge_no,patient_id):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    patient_info = get_object_or_404( PatientRegister,patient_id=patient_id)
    disch = get_object_or_404(Discharge, Discharge_no=discharge_no)
    history = PatientHistory.objects.filter(Patient_ID=patient_info.patient_id)
    lab = Laboratory.objects.filter(PatientID=patient_info.patient_id)
    prec = Prescription.objects.filter(PatientID=patient_info.patient_id)
    return render(request,'admin_dash/refere_info.html',{'notifications':notifications,
                                                         'unseen_count':unseen_count,
                                                         'patient_info':patient_info,
                                                         'disch':disch,
                                                         'histories':history,
                                                         'laboratories':lab,
                                                         'prescriptions':prec}
                  )
# @login_required
def dis_index(request):
    total_sum = PaymentModel.objects.aggregate(total_sum=Sum('Total'))['total_sum']
    total_sum = total_sum or 0
    number_of_patient = PatientRegister.objects.count()
    number_of_app= Appointment.objects.count()
    number_of_history = PatientHistory.objects.count()
    number_of_Presc= Prescription.objects.count()
    number_of_lab= Laboratory.objects.count()
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    unseen_feedbacks = Feedback.objects.filter(Is_seen=False)
    unseen_feedbacks_count = Feedback.objects.filter(Is_seen=False).count()
    cash_total_sums = PaymentModel.objects.filter(Pay_method='Cash').aggregate(total_sum=Sum('Total'))
    cash_total_sum = cash_total_sums['total_sum'] or 0
    insurance_total_sums = PaymentModel.objects.filter(Pay_method='Insurance').aggregate(total_sum=Sum('Total'))
    insurance_total_sum = insurance_total_sums['total_sum'] or 0
    number_of_cancelled= Appointment.objects.filter(App_status='Cancelled').count()
    number_of_pending= Appointment.objects.filter(App_status='Pending').count()
    number_of_completed= Appointment.objects.filter(App_status='Completed').count()
    current_year = datetime.now().year

    # Create a list of years from 2022 to the current year
    years = list(range(2022, current_year + 1))

    # Query the database to count registrations for each year
    registration_counts = [
        {
            'year': year,
            'count': Appointment.objects.filter(App_date__year=year).count()  # Replace YourModel and date_of_registration with your actual model and field names
        }
        for year in years
    ]
    context= {'registration_counts':registration_counts}
    return render(request,'admin_dash/index.html',{'number_patients':number_of_patient,
                                                   'number_of_app':number_of_app,
                                                   'total_amount':total_sum,
                                                   'notifications':notifications,
                                                   'unseen_count':unseen_count,
                                                   'unseen_feedbacks':unseen_feedbacks,
                                                   'unseen_feedbacks_count':unseen_feedbacks_count,
                                                   'number_of_history':number_of_history,
                                                   'number_of_Presc':number_of_Presc,
                                                   'cash_total_sum':cash_total_sum,
                                                   'insurance_total_sum':insurance_total_sum,
                                                   'number_of_lab':number_of_lab,
                                                   'context':context,
                                                   'number_of_cancelled':number_of_cancelled,
                                                   'number_of_pending':number_of_pending,
                                                   'number_of_completed':number_of_completed,
                                                   })

def display_users(request):
    users = UserProfileInfo.objects.all()
    combined_data = []
    for user_info in users:
        # Check if the user has role and specialty information in UserProfileInfo2
        if user_info.role and user_info.specialty:
            user_dict = {
                'first_name': user_info.user.first_name,
                'last_name': user_info.user.last_name,
                'email': user_info.user.email,
                'role': user_info.role,
                'id': user_info.user.id,
                'special': user_info.specialty,
                'is_active': user_info.user.is_active,
            }
            combined_data.append(user_dict)
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    return render(request, 'admin_dash/staffs.html', {'combined_datas': combined_data,
                                                       'notifications': notifications,
                                                       'unseen_count': unseen_count})

# @login_required
def dis_user_registration(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    return render(request,'admin_dash/add-staff.html',{'notifications':notifications,
                                                    'unseen_count':unseen_count})
def dis_web_home(request):
    return render(request,'admin_dash/web_home.html')
def edit_staff(request):
    return render(request,'admin_dash/edit_staff.html')
# @login_required
def view_staff(request,user_id):
    user = get_object_or_404(User, pk=user_id)
    user_profile_info = get_object_or_404(UserProfileInfo, user_id=user_id)
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    return render(request,'admin_dash/view_staff.html',{'users':user,
                                                        'user_profile_info':user_profile_info,
                                                        'notifications':notifications,
                                                    'unseen_count':unseen_count})


# @login_required
def change_credentials(request):
    if request.method == 'POST':
        username = request.POST['username']
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        user = request.user  # Use the authenticated user directly
        user_profile = UserProfileInfo.objects.get(user=user)
        # Verify the current password
        if user.check_password(current_password):
            if new_password == confirm_new_password:
                # Update username and password
                user.username = username
                user.set_password(new_password)
                user.save()

                # Optional: Update user profile if necessary
                user_profile.password_changed = True
                user_profile.save()

                # Re-authenticate user with new password
                login(request, user)

                # Redirect to login page after successful update
                return redirect('user_log')
            else:
                error_message = "New passwords must match."
        else:
            error_message = "Incorrect current password."

        # Render the form with error message
        return render(request, 'admin_dash/change_credentials.html', {'error_message': error_message})

    return render(request, 'admin_dash/change_credentials.html')

def success_message(request):
    # You can customize this view to display a success message or redirect to a different page
    return HttpResponse("Password changed successfully.")

# @login_required
def save_data(request, format):
    queryset = PatientRegister.objects.all()  # Fetch data from your model

    if format == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

        writer = csv.writer(response)
        writer.writerow(['Patient_ID', 'First_Name', 'Middle_Name','Last_Name', 'Age', 'Phone_No'])  # Write header row
        for obj in queryset:
            writer.writerow([obj.patient_id, obj.first_name,obj.middle_name, obj.last_name,obj.age,obj.phone_number,])  # Write data rows

        return response

    elif format == 'pdf':
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="data.pdf"'

        doc = SimpleDocTemplate(response, pagesize=letter)
        table_data = []
        for obj in queryset:
            table_data.append([obj.patient_id, obj.first_name,obj.middle_name, obj.last_name,obj.age,obj.phone_number,])  # Add data rows to table

        table = Table(table_data)
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])
        table.setStyle(style)
        doc.build([table])

        return response

    elif format == 'excel':
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="data.xlsx"'

        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        for idx, obj in enumerate(queryset, start=1):
            worksheet[f'A{idx}'] = obj.patient_id
            worksheet[f'B{idx}'] = obj.first_name
            worksheet[f'C{idx}'] = obj.middle_name
            worksheet[f'D{idx}'] = obj.last_name
            worksheet[f'E{idx}'] = obj.age
            worksheet[f'F{idx}'] = obj.phone_number

        workbook.save(response)
        return response

    else:
        # Handle other formats or invalid requests here
        return HttpResponse("Invalid format requested")
    
# @login_required
def deactivate(request, user_id):
    user_deactive = get_object_or_404(User, id=user_id)
    user_deactive.is_active = False
    user_deactive.save()
    return redirect('display_users')





