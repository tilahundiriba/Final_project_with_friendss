from django.shortcuts import render

def write_feedback(request):
    return render(request,'patient/write_feedback.html')
def patient_dash(request):
    return render(request,'patient/patient_dash.html')
