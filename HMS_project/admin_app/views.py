
from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import LabTest,Payment
from django.utils.crypto import get_random_string
from django.contrib.auth import login
from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from HMS_project import settings
from .models import UserAccount1
from .utils import generate_username, generate_password
from .models import UserAccount1 
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import UserProfileInfo2
from .models import Patient

from django.contrib.auth import authenticate, login
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
                    # User authentication successful and profession matches
                    login(request, user)
                    return HttpResponse('User logined successfully') # Redirect to home URL after login
                else:
                    return HttpResponse('Invalid profession for the user')
            except UserProfileInfo2.DoesNotExist:
                return HttpResponse('User does not have a profile')
        else:
            # User authentication failed
            return HttpResponse('Invalid username or password')
    else:
        return render(request, 'admin_dash/test_login.html', {})



def register(request):
    registered = False
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        profession = request.POST.get('profession')  # Retrieve profession from the form
        protfolio_site = request.POST.get('protfolio_site')
        profile_pic = request.FILES.get('profile_pic')

        # Create user object
        user = User.objects.create_user(username=username, email=email, password=password)

        # Create user profile
        user_profile = UserProfileInfo2.objects.create(
            user=user,
            profession=profession,
            protfolio_site=protfolio_site,
            profile_pic=profile_pic
        )

        registered = True
        # return redirect('dis_dash_content')
    else:
        # Render an empty form for GET request
        return render(request, 'admin_dash/test_reg.html')

    return render(request, 'admin_dash/test_reg.html',
                  {'registered': registered})









def createUserAccount(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        profession = request.POST.get('profession')

        # Generate username and password
        username = generate_username(email, profession)
        password = generate_password()

        # Create the user
        hashed_password = make_password(password)
        user = UserAccount1.objects.create(
            UserName=username,
            Password=hashed_password,
            Email=email,
            Profession=profession,
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



# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  
#             return redirect('home')  
#     else:
#         form = SignUpForm()
#     return render(request, 'admin_app/register.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         username= request.POST.get('username')
#         profession= request.POST.get('profession')
#         password= request.POST.get('password')

#         user = authenticate(username=username, profession=profession,password=password)

#         if user:
#             if user.is_active:
#                 login(request,user)
#                 return HttpResponseRedirect(reverse('dis_home'))
#             else:
#                 return HttpResponse('accont not active')
#         else:
#             print('some tried to login and failed!')
#             print('username:{} and password{} and profession{}'.format(username,password,profession))
#             return HttpResponse('invalid login details supplied!')
#     else:
#         return render(request , 'admin_app/loginfinal.html',{})

    
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
# doctor dashboard views
def dis_dr_dash(request):
    return render(request,'doctors/dr_dash.html')
def dis_dr_dash_content(request):
    return render(request,'doctors/dash_content.html')
# user register views
def form(request):
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
        street_address = request.POST.get('street_address')

        # Generate unique ID
        generated_id = 'SH' + get_random_string(length=6, allowed_chars='1234567890')

        # Save patient data to the database
        patient = Patient.objects.create(
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
            street_address=street_address
        )

        #return render(request, 'doctors/form.html', {'generated_id': generated_id})

    return render(request,'doctors/form.html')

def dis_patient_history(request):
    
    return render(request,'doctors/patient_history.html')
# additional forms
def dis_bill(request):
    return render(request,'doctors/bill.html')
def dis_medication(request):
    return render(request,'doctors/medication.html')



def dis_user_registration(request):
    return render(request,'admin_dash/user_registration.html')
def dis_vital_info(request):
    return render(request,'doctors/vital_info.html')
