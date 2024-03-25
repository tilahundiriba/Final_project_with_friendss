
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
from .models import UserProfileInfo2
# from .models import PatientChange
from django.http import HttpResponse, HttpResponseRedirect
from .models import BedAllocation
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
from doctor_app.models import Appointment
from casher_app.models import PaymentModel
import csv
import openpyxl
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table,TableStyle
from reportlab.lib import colors

def writenotification(request):
    return render(request, 'doctor/view_notification.html')
class NotificationListView(View):
    def get(self, request, *args, **kwargs):
        # Retrieve all notifications from the database
        notifications = Notification.objects.all()
        
        # Create a list to store the notification messages
        notification_messages = []
        
        # Iterate over the notifications and extract the messages
        for notification in notifications:
            notification_messages.append(notification.message)
        
        # Return the notification messages as a JSON response
        return JsonResponse(notification_messages, safe=False)

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
                user_profile = UserProfileInfo2.objects.get(user=user)
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
                    return redirect('change_credentials')
                # else:
                #     return HttpResponse('Invalid profession for the user')
            except UserProfileInfo2.DoesNotExist:
                return HttpResponse('User does not have a role...!!!')

        else:
            # User authentication failed
            return HttpResponse('Invalid username or password')
    else:
        return render(request, 'admin_dash/login.html', {})

# @login_required
def logout_view(request):
    logout(request)
    return redirect('user_log')

def createUserAccount(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        role = request.POST.get('role')
        special = request.POST.get('spec')
        # Generate username and password
        username = generate_username(email, role)
        password = generate_password()

        # Create the user
        hashed_password = make_password(password)
        user = User.objects.create_user(username=username, email=email, password=password)

        # Create user profile
        user_profile = UserProfileInfo2.objects.create(
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

        # Redirect to account list after account creation
        return redirect('dis_dash_content')

    return render(request, 'admin_dash/user_registration2.html')
def dis_login2(request):
    return render(request,'admin_dash/login.html')
def dis_base(request):
    return render(request,'admin_app/base.html')
# admin dashboard views
def dis_dash(request):
    return render(request,'admin_dash/dashboard.html')
def dis_dash_content(request):
    return render(request,'admin_dash/dash_content.html')
def dis_index(request):
    total_sum = PaymentModel.objects.aggregate(total_sum=Sum('Total'))['total_sum']
    total_sum = total_sum or 0
    number_of_patient = PatientRegister.objects.count()
    number_of_app= Appointment.objects.count()
    return render(request,'admin_dash/index.html',{'number_patients':number_of_patient,
                                                   'number_of_app':number_of_app,
                                                   'total_amount':total_sum})
#admin views end here

# doctor views start here
# doctor dashboard views start here

def display_users(request):
    users= UserProfileInfo2.objects.all()
    user_names= User.objects.all()
    combined_data = []
    for user_info in users or user_names:
        user_dict = {
            'username': user_info.user.username,
            'email': user_info.user.email,
            'role': user_info.role,
            'id':user_info.user.id,
            'special':user_info.specialty,
        }
        combined_data.append(user_dict)
    return render(request,'admin_dash/staffs.html',{'combined_datas':combined_data})
def dis_user_registration(request):
    return render(request,'admin_dash/user_registration2.html')
def dis_web_home(request):
    return render(request,'admin_dash/web_home.html')



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

@login_required
def change_credentials(request):
    if request.method == 'POST':
        username = request.POST['username']
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        user = request.user  # Use the authenticated user directly
        user_profile = UserProfileInfo2.objects.get(user=user)
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



# views.py


def bed_allocation_detail(request):
    bed_allocation_instance = BedAllocation.objects.all()
    return render(request, 'admin_app/testNodays.html', {'bed_allocation_instance': bed_allocation_instance})

# view for handling the document saving format start
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