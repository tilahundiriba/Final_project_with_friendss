from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from.models import RoomInformation,VitalInformation
def dis_medication(request):
    return render(request,'nurse_dash/medication2.html')
def dis_vital_info(request):
    registered=False
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        vital_no = request.POST.get('VIN')
        date = request.POST.get('date')
        Heart_Rate = request.POST.get('Heart_Rate')
        bloodpre = request.POST.get('bloodpre')
        resRate = request.POST.get('resRate')
        bodytemp = request.POST.get('bodytemp')
        oxysatu = request.POST.get('oxysatu')
        painlev = request.POST.get('painlev')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        bloodglu = request.POST.get('bloodglu')
        nurse_id = request.POST.get('nurseid')
        remark = request.POST.get('remark')
        
        vital = VitalInformation(
            Patient_ID=patient_id,
            Vital_info_no=vital_no,
            H_rate=Heart_Rate,
            B_pressure=bloodpre,
            Body_temp=bodytemp,
            Pain_level=painlev,
            Weight=weight,
            Height=height,
            Nurse_id=nurse_id,
            Oxy_satu=oxysatu,
            B_gluc_level=bloodglu,
            R_rate=resRate,
            D_record=date,
            Remark=remark,
        )
        vital.save()
        registered=True
        return render(request,'nurse_dash/vital_info2.html',{'registered':registered}) # Redirect to a success page or another URL
    return render(request,'nurse_dash/vital_info2.html')
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
        return render(request,'nurse_dash/add-room.html',{'registered':registered})  # Redirect to a success page or another URL
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
