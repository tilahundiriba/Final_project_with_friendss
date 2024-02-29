from django.shortcuts import render

def dis_lab_dash(request):
    return render(request, 'laboratory_dash/lab_dashboard.html')
def dis_lab_dash_content(request):
    return render(request, 'laboratory_dash/lab_dash_content.html')