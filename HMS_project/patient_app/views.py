from django.shortcuts import render

def write_feedback(request):
    return render(request,'patient/write_feedback.html')
