from django.shortcuts import render
from .models import  Appointment,Prescription
from receptionist_app.models import PatientRegister
from django.shortcuts import get_object_or_404
from admin_app.models import UserProfileInfo2

def dis_dr_dash(request):
    return render(request,'doctor/dr_dash.html')


def add_perscription(request):
    registered=False
    if request.method == 'POST':
        patientid = request.POST.get('patient_id')
        prec_number = request.POST.get('pec_no')
        prec_date = request.POST.get('pres_date')
        p_name = request.POST.get('name')
        doctor_id = request.POST.get('dr_name')
        prec = request.POST.get('prescription')
        
     
        # Extract other fields similarly
        
        # Create an instance of Appointment model and save it
        patient = get_object_or_404( PatientRegister,patient_id=patientid)
        doctor = get_object_or_404(UserProfileInfo2, user_id=doctor_id)
        appointment = Prescription(
            PatientID=patient,
            Prec_date=prec_date,
            Prec_number=prec_number,
            Doctor_ID=doctor,
            Patient_full_name=p_name,
            Precscriptions=prec,

            # Assign values to other fields similarly
        )
        appointment.save()
        registered=True
        # return redirect('add-appointment') 
        return render(request,'doctor/add-perscription.html',{'register':registered})
    return render(request,'doctor/add-perscription.html')
def edit_perscription(request):
    return render(request,'doctor/edit-perscription.html')
def perscription(request):
    prescription= Prescription.objects.all()
    return render(request,'doctor/perscriptions.html',{'prescriptions':prescription})
def about_perscription(request):
    return render(request,'doctor/about-perscription.html')

def dis_dr_dash_content(request):
    return render(request,'doctor/dash_content.html')
def dis_patient_history(request):


    return render(request,'doctor/patient_history.html')
def add_appointment(request):
    return render(request,'doctor/add-appointment.html')
def edit_appointment(request):
    return render(request,'doctor/edit-appointment.html')
def dis_appointment(request):
    appointment=Appointment.objects.all()
    return render(request,'doctor/appointments.html',{'appointment':appointment})
def about_appointment(request):
    
    return render(request,'doctor/about-appointment.html')
def dis_patient_history(request):
    return render(request,'doctor/patient_history.html')


from django.shortcuts import render, redirect
from .models import Appointment

def create_appointment(request):
    registered=False
    if request.method == 'POST':
        patientid = request.POST.get('patient_id')
        app_number = request.POST.get('app_no')
        app_date = request.POST.get('app_date')
        time_slot = request.POST.get('time_slot')
        doctor_id = request.POST.get('dr_name')
        app_reseon = request.POST.get('problem')
        app_status = request.POST.get('status')
     
        # Extract other fields similarly
        
        # Create an instance of Appointment model and save it
        patient = get_object_or_404( PatientRegister,patient_id=patientid)
        doctor = get_object_or_404(UserProfileInfo2, user_id=doctor_id)
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
        return render(request, 'doctor/add-appointment.html',{'registered':registered}) # Redirect to a success page or another URL

    return render(request, 'doctor/add-appointment.html')

