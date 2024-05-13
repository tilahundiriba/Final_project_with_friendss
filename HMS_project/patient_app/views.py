from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from admin_app.models import Feedback,Notification,UserProfileInfo
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
        patients = PatientRegister.objects.get(patient_id=patient_id)
        try:
            appointments = Appointment.objects.filter(PatientID=patient_id).latest('App_date')
        except Appointment.DoesNotExist:
            appointments = None  # Or handle the absence of appointments in another way

        try:
            labs = Laboratory.objects.filter(PatientID=patient_id).latest('Admit_date')
        except Laboratory.DoesNotExist:
            labs = None  # Or handle the absence of laboratory records in another way

        return render(request, 'patient/patient_info.html', {
            'patients': patients,
            'appointments': appointments,
            'labs': labs
        })
    return render(request, 'patient/patient_info.html')
def patient_dash(request):
    users = UserProfileInfo.objects.filter(role='doctor')
    combined_data = []
    for user_info in users:
        # Check if the user has role and specialty information in UserProfileInfo2
        if user_info.role and user_info.specialty:
            user_dict = {
                'first_name': user_info.user.first_name,
                'last_name': user_info.user.last_name,
                'email': user_info.user.email,
                'role': user_info.role,
                'special': user_info.specialty,
                'profile': user_info.profile_pic.url,

            }
            combined_data.append(user_dict)
    return render(request,'patient/patient_dash.html',{'combined_data':combined_data})
def display_feedback(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(Seen=False).count()
    unseen_feedbacks = Feedback.objects.filter(Is_seen=False)
    return render(request,'admin_dash/display_feedback.html',{'unseen_feedbacks':unseen_feedbacks,
                                                              'notifications':notifications,
                                                              'unseen_count':unseen_count})
def mark_as_read(request,added_no):
    patient_info = get_object_or_404( Feedback,Added_no=added_no)
    patient_info.Is_seen=True
    patient_info.save()
    return redirect('dis_dash')
