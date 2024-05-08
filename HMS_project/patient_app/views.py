from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from admin_app.models import Feedback
from receptionist_app.models import PatientRegister
from doctor_app.models import Appointment,PatientHistory,Laboratory
from django.core.exceptions import ObjectDoesNotExist
def write_feedback(request):
    feedback=False
    if request.method == 'POST':
        name = request.POST.get('name')
        feedback = request.POST.get('message')
        email = request.POST.get('email')
        feed= Feedback(
            Name=name,
            Feedback = feedback,
            Email = email
        )
        feed.save()
        feedback=True
        return render(request,'patient/write_feedback.html',{'feedback':feedback})
    return render(request,'patient/write_feedback.html',{'feedback':feedback})


def Patient_info(request):
    if request.method == 'POST':
        patient_id = request.POST.get('search_query')
        try:
            patients = PatientRegister.objects.get(patient_id=patient_id)
            appointments = Appointment.objects.get(PatientID=patient_id)
            labs = Laboratory.objects.get(PatientID=patient_id)
        except ObjectDoesNotExist as e:
            # Handle the case where appointments or labs do not exist for the patient
            appointments = None
            labs = None
        return render(request, 'patient/patient_info.html', {
            'patients': patients,
            'appointments': appointments,
            'labs': labs
        })
    return render(request, 'patient/patient_info.html')
def patient_dash(request):

    return render(request,'patient/patient_dash.html')
def mark_as_read(request,added_no):
    patient_info = get_object_or_404( Feedback,Added_no=added_no)
    patient_info.Is_seen=True
    patient_info.save()
    return redirect('dis_dash')
