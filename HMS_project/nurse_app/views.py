from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from admin_app .models import UserProfileInfo2
from receptionist_app.models import PatientRegister
from.models import RoomInformation,VitalInformation,Medication,BedInformation
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def nurse_profile(request):
    user = request.user
    return render(request, 'nurse_dash/profile.html', {'user': user})

@login_required
def nurse_profile_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.user != user:  # Ensure user can only update their own profile
        return redirect('show_nurse_profile')
    
    user_profile, created = UserProfileInfo2.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        user_profile.profile_pic = profile_pic
        user_profile.save()
        return redirect('show_nurse_profile')
    
    return render(request, 'nurse_dash/update_profile.html', {'user_id': user_id, 'user_profile': user_profile})


def add_medication(request):
    users= User.objects.all()
    registered=False
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        med_time = request.POST.get('MediTime')
        bed_no = request.POST.get('Bedno')
        drug = request.POST.get('drugs')
        nurse_name = request.POST.get('nurseid')
        remark = request.POST.get('remark')
      
        patient = get_object_or_404( PatientRegister,patient_id=patient_id)
        nurse_name = get_object_or_404( User,username=nurse_name)
        med = Medication(
            Patient_id=patient,
            Med_time=med_time,
            Bed_no=bed_no,
            Remark=remark,
            Nurse_name=nurse_name,
            Drugs=drug,
           
        )
        med.save()
        registered=True
        return render(request,'nurse_dash/add_medication.html',{'registered':registered,'users':users})
    return render(request,'nurse_dash/add_medication.html',{'users':users})
def dis_medication(request):
    medications = Medication.objects.all()
    return render(request,'nurse_dash/dis_medication.html',{'medications':medications})
def edit_medication(request,med_no):
    medications = Medication.objects.get(Med_no=med_no)
    users= User.objects.all()
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        med_time = request.POST.get('MediTime')
        bed_no = request.POST.get('Bedno')
        drug = request.POST.get('drugs')
        nurse_name = request.POST.get('nurseid')
        remark = request.POST.get('remark')
        nurse_name = get_object_or_404( User,username=nurse_name)
        patient = get_object_or_404( PatientRegister,patient_id=patient_id)
    
        medications.Patient_id=patient
        medications.Med_time=med_time
        medications.Bed_no=bed_no
        medications.Remark=remark
        medications.Nurse_name=nurse_name
        medications.Drugs=drug
        medications.save()
        return redirect('dis_medication')
    return render(request,'nurse_dash/edit_medication.html',{'medications':medications,'users':users})
def add_vital_info(request):
    users= User.objects.all()
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
        nurse_name = request.POST.get('nurseid')
        remark = request.POST.get('remark')
        patient = get_object_or_404( PatientRegister,patient_id=patient_id)
        nurse_name = get_object_or_404( User,username=nurse_name)
        vital = VitalInformation(
            Patient_id=patient,
            Vital_info_no=vital_no,
            H_rate=Heart_Rate,
            B_pressure=bloodpre,
            Body_temp=bodytemp,
            Pain_level=painlev,
            Weight=weight,
            Height=height,
            Nurse_id=nurse_name,
            Oxy_satu=oxysatu,
            B_gluc_level=bloodglu,
            R_rate=resRate,
            D_record=date,
            Remark=remark,
        )
        vital.save()
        registered=True
        return render(request,'nurse_dash/add-vital_info.html',{'registered':registered}) # Redirect to a success page or another URL
    return render(request,'nurse_dash/add-vital_info.html',{'users':users})
def add_room(request):
    registered=False
    if request.method == 'POST':
        room_block = request.POST.get('block_no')
        room_no = request.POST.get('room_no')
        bed_no = request.POST.get('bed_no')
        status = request.POST.get('status')
        room_type = request.POST.get('room-type')
        room_info = RoomInformation(
            Room_block=room_block,
            Room_no=room_no,
            Bed_no=bed_no,
            Status=status,
            Room_type=room_type,
        )
        room_info.save()
        registered=True
        return render(request,'nurse_dash/add-room.html',{'registered':registered})  # Redirect to a success page or another URL
    return render(request,'nurse_dash/add-room.html')
def edit_room(request,bed_no):
    rooms = RoomInformation.objects.get(Bed_no=bed_no)
    if request.method == 'POST':
        room_block = request.POST.get('block_no')
        room_no = request.POST.get('room_no')
        bed_noo = request.POST.get('bed_no')
        status = request.POST.get('status')
        room_type = request.POST.get('room-type')
        rooms.Room_block=room_block
        rooms.Room_no=room_no
        rooms.Bed_no=bed_noo
        rooms.Status=status
        rooms.Room_type=room_type
        rooms.save()
        return redirect('dis_room')
    return render(request,'nurse_dash/edit-room.html',{'rooms':rooms})
def dis_room(request):
    room =RoomInformation.objects.all()
    return render(request,'nurse_dash/rooms.html',{'rooms':room})
def allocate_room(request):
    registered=False
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        room_no = request.POST.get('room-number')
        bed_no = request.POST.get('bed_no')
        all_date = request.POST.get('allot-date')
        room_type = request.POST.get('room-type')
        patient = get_object_or_404( PatientRegister,patient_id=patient_id)
        room = get_object_or_404( RoomInformation,Room_no=room_no)
        bed_info = BedInformation.objects.create(
            Patient_id=patient,
            Room_no=room,
            Bed_no=bed_no,
            Alloc_date=all_date,
            Room_type=room_type,
        )
        registered=True
        return render(request,'nurse_dash/Room_allocation.html',{'registered':registered})
    return render(request,'nurse_dash/Room_allocation.html')
def dis_bed_allocation(request):
    alloc =BedInformation.objects.all()
    return render(request,'nurse_dash/allocations.html',{'allocs':alloc})
def dis_vitals(request):
    vitals =VitalInformation.objects.all()
    return render(request,'nurse_dash/vital_infos.html',{'vitals':vitals})
def nurse_dash(request):
    return render(request,'nurse_dash/nurse_dash.html')
def dis_nurse_dash_content(request):
    return render(request,'nurse_dash/dash_content.html')
