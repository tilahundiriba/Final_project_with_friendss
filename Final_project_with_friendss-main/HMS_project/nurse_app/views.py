from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from.models import RoomInformation
def dis_medication(request):
    return render(request,'nurse_dash/medication.html')
def dis_vital_info(request):
    return render(request,'nurse_dash/vital_info.html')
def add_room(request):
    registered=False
    if request.method == 'POST':
        room_block = request.POST.get('block_no')
        room_no = request.POST.get('room_no')
        bed_no = request.POST.get('bed_no')
        status = request.POST.get('status')
        appointment = RoomInformation(
            Room_block=room_block,
            Room_no=room_no,
            Bed_no=bed_no,
            Status=status,
        )
        appointment.save()
        registered=True
        return redirect('dis_nurse_dash_content')  # Redirect to a success page or another URL
    return render(request,'nurse_dash/add-room.html')
def edit_room(request):
    return render(request,'nurse_dash/edit-room.html')
def dis_room(request):
    room =RoomInformation.objects.all()
    return render(request,'nurse_dash/rooms.html',{'rooms':room})
def nurse_dash(request):
    return render(request,'nurse_dash/nurse_dash.html')
def dis_nurse_dash_content(request):
    return render(request,'nurse_dash/dash_content.html')
