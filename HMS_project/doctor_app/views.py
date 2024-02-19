from django.shortcuts import render


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
    return render(request,'doctor/appointments.html')
def about_appointment(request):
    return render(request,'doctor/about-appointment.html')
def dis_patient_history(request):
    return render(request,'doctor/patient_history.html')
