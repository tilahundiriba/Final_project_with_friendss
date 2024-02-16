
from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import LabTest,Payment
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from HMS_project import settings
from .models import UserAccount1
from .utils import generate_username, generate_password
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
        html_message = render_to_string('userAccountApp/email_templte.html', context)
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
        return redirect('createUserAccount')

    return render(request, 'admin_app/register.html')



def members(request):
    return HttpResponse("Hello From Admin App!")
def testing(request):
       context = {
          'fruits': ['Apple', 'Banana', 'Cherry'],   
        }
       return render(request,'admin_app/templates.html',context)



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
def home(request):
    return render(request,'admin_app/home.html')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')  
    else:
        form = SignUpForm()
    return render(request, 'admin_app/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(username=username , password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('test'))
            else:
                return HttpResponse('accont not active')
        else:
            print('some tried to login and failed!')
            print('username:{} and password{}'.format(username,password))
            return HttpResponse('invalid login details supplied!')
    else:
        return render(request , 'admin_app/home.html',{})
def dis_login(request):
    return render(request,'admin_app/loginfinal.html')
def dis_home(request):
    return render(request,'admin_app/homefinal.html')
def dis_homepage(request):
    return render(request,'admin_app/homepage.html')
def dis_base(request):
    return render(request,'admin_app/base.html')

def dis_dash(request):
    return render(request,'admin_dash/dashboard.html')
def dis_dash_content(request):
    return render(request,'admin_dash/dash_content.html')

def dis_dr_dash(request):
    return render(request,'doctors/dr_dash.html')
def dis_dr_dash_content(request):
    return render(request,'doctors/dash_content.html')
def form(request):
    return render(request,'doctors/form.html')
