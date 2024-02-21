
from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import LabTest,Payment
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
from .models import Patient
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        profession = request.POST.get('profession')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if user's profession matches
            try:
                user_profile = UserProfileInfo2.objects.get(user=user)
                if user_profile.profession == profession:
                    return HttpResponse('User logged in successfully') 
                    if user_profile.password_changed:
                        login(request, user)
                        return HttpResponse('User logged in successfully')  # Redirect to home URL after login
                    else:
                        # Redirect to change password view
                        return render(request, 'admin_app/change_credentials.html', {})
                else:
                    return HttpResponse('Invalid profession for the user')
            except UserProfileInfo2.DoesNotExist:
                return HttpResponse('User does not have a profile')

        else:
            # User authentication failed
            return HttpResponse('Invalid username or password')
    else:
        return render(request, 'admin_dash/loginfinal.html', {})



# def register(request):
#     registered = False
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         profession = request.POST.get('profession')  # Retrieve profession from the form
#         # protfolio_site = request.POST.get('protfolio_site')
#         # profile_pic = request.FILES.get('profile_pic')

#         # Create user object
#         user = User.objects.create_user(username=username, email=email, password=password)

#         # Create user profile
#         user_profile = UserProfileInfo2.objects.create(
#             user=user,
#             profession=profession,
#             # protfolio_site=protfolio_site,
#             # profile_pic=profile_pic
#         )

#         registered = True
#         # return redirect('dis_dash_content')
#     else:
#         # Render an empty form for GET request
#         return render(request, 'admin_dash/test_reg.html')

#     return render(request, 'admin_dash/test_reg.html',
#                   {'registered': registered})
def createUserAccount(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        profession = request.POST.get('profession')
        # Generate username and password
        username = generate_username(email, profession)
        password = generate_password()

        # Create the user
        hashed_password = make_password(password)
        user = User.objects.create_user(username=username, email=email, password=password)

        # Create user profile
        user_profile = UserProfileInfo2.objects.create(
            user=user,
            profession=profession,
        )
        # Send email with username and password
        context = {
            'username': username,
            'password': password,
            'profession': profession,
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

    return render(request, 'admin_dash/user_registration.html')


def lab_test_payment(request):
    lab_tests = LabTest.objects.all()
    context = {'lab_tests': lab_tests}
    return render(request, 'admin_app/lab_test_payment.html', context)

def process_payment(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        lab_test_id = request.POST.get('lab_test_type')
        payment_amount = request.POST.get('payment_amount')

        lab_test = LabTest.objects.get(id=lab_test_id)
        payment = Payment.objects.create(
            patient_name=patient_name,
            lab_test=lab_test,
            payment_amount=payment_amount
        )
        return HttpResponse("Payment processed successfully!")

    return HttpResponse("Invalid request method.")



def members(request):
    return HttpResponse("Hello From Admin App!")
def testing(request):
       context = {
          'fruits': ['Apple', 'Banana', 'Cherry'],   
        }
       return render(request,'admin_app/templates.html',context)



# def lab_test_payment(request):
    # lab_tests = LabTest.objects.all()
    # context = {'lab_tests': lab_tests}
    # return render(request, 'admin_app/lab_test_payment.html', context)
# 
# def process_payment(request):
    # if request.method == 'POST':
        # patient_name = request.POST.get('patient_name')
        # lab_test_id = request.POST.get('lab_test_type')
        # payment_amount = request.POST.get('payment_amount')
# 
        # lab_test = LabTest.objects.get(id=lab_test_id)
        # payment = Payment.objects.create(
            # patient_name=patient_name,
            # lab_test=lab_test,
            # payment_amount=payment_amount
        # )
        # return HttpResponse("Payment processed successfully!")
# 
    # return HttpResponse("Invalid request method.")

def home(request):
    return render(request,'admin_app/home.html')
def dis_login(request):
    return render(request,'admin_app/loginfinal.html')
def dis_home(request):
    return render(request,'admin_app/homefinal.html')
def dis_homepage(request):
    return render(request,'admin_app/homepage.html')
def dis_base(request):
    return render(request,'admin_app/base.html')

# admin dashboard views
def dis_dash(request):
    return render(request,'admin_dash/dashboard.html')
def dis_dash_content(request):
    return render(request,'admin_dash/dash_content.html')
def dis_index(request):
    return render(request,'admin_dash/index.html')
#admin views end here

# doctor views start here
# doctor dashboard views start here

def displayRegisteredPatient(request):
    return render(request,'doctors/displayRegisteredPatient.html')
def dis_user_registration(request):
    return render(request,'admin_dash/user_registration.html')




@login_required
def change_credentials(request):
    if request.method == 'POST':
        username = request.POST['username']
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        user = authenticate(request, username=request.user.username, password=current_password)
        user_profile = UserProfileInfo2.objects.get(user=user)
        if user is not None:
            
            if new_password == confirm_new_password:
                user.set_password(new_password)
                user.username = username
                user.user_profile.password_changed = True
                user.save()
                user.user_profile.save()
                login(request, user)
                # return render(request, 'admin_app/loginfinal.html')
                # return HttpResponse("password changed successfully.")
                return redirect('login')
            else:
                error_message = "New passwords must match."
                return render(request, 'admin_app/change_credentials.html', {'error_message': error_message})
        else:
            error_message = "Incorrect current password."
            return render(request, 'admin_app/change_credentials.html', {'error_message': error_message})
    return render(request, 'admin_app/change_credentials.html')
def success_message(request):
    # You can customize this view to display a success message or redirect to a different page
    return HttpResponse("Password changed successfully.")