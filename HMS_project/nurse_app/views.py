from django.shortcuts import render

def dis_medication(request):
    return render(request,'nurse_dash/medication.html')
def dis_vital_info(request):
    return render(request,'nurse_dash/vital_info.html')
def add_room(request):
    return render(request,'nurse_dash/add-room.html')
def edit_room(request):
    return render(request,'nurse_dash/edit-room.html')
def dis_room(request):
    return render(request,'nurse_dash/rooms.html')
def nurse_dash(request):
    return render(request,'nurse_dash/nurse_dash.html')
def dis_nurse_dash_content(request):
    return render(request,'nurse_dash/dash_content.html')
