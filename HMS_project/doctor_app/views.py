from django.shortcuts import render
from .models import  Appointment
from receptionist_app.models import Patient
from django.shortcuts import get_object_or_404
from admin_app.models import UserProfileInfo2

def dis_dr_dash(request):
    return render(request,'doctor/dr_dash.html')
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
        patient = get_object_or_404(Patient, patient_id=patientid)
        doctor = get_object_or_404(UserProfileInfo2, user_id=doctor_id)
        appointment = Appointment(
            P_ID=patient,
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
        return redirect('add-appointment')  # Redirect to a success page or another URL

    return render(request, 'doctor/add-appointment.html')

