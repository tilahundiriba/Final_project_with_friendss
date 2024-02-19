from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.shortcuts import render
from .models import Patient

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
        # doctor_id = request.POST.get('doctor_id')
        # doctors = UserAccount1.objects.filter(account_type='Doctor')

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
            street_address=street_address,
        )

        #return render(request, 'doctors/form.html', {'generated_id': generated_id})

    return render(request,'receptionist_dash/form.html')
def receptionist_dash(request):
    return render(request,'receptionist_dash/receptionist_dash.html')
def receptionist_dash_content(request):
    return render(request,'receptionist_dash/dash_content.html')
def add_patient(request):
    return render(request,'receptionist_dash/add-patient.html')
def dis_patient(request):
    return render(request,'receptionist_dash/patients.html')
def about_patient(request):
    return render(request,'receptionist_dash/about-patient.html')
def edit_patient(request):
    return render(request,'receptionist_dash/edit-patient.html')
def dis_forms(request):
    return render(request,'receptionist_dash/forms.html')
