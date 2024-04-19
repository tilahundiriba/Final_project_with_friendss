from django.shortcuts import render,redirect
from .models import PaymentModel,ServicePayment,Discharge
from django.shortcuts import get_object_or_404
from admin_app.models import UserProfileInfo2,Notification
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from receptionist_app.models import PatientRegister

@login_required
def profile(request):
    user = request.user
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request, 'casher_dash/profile.html', {'user': user,
                                                        'notifications':notifications,
                                                        'unseen_count':unseen_count})

@login_required
def casher_profile_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.user != user:  # Ensure user can only update their own profile
        return redirect('show_casher_profile')
    
    user_profile, created = UserProfileInfo2.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        user_profile.profile_pic = profile_pic
        user_profile.save()
        return redirect('show_casher_profile')
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request, 'casher_dash/update_profile.html', {'user_id': user_id, 
                                                               'user_profile': user_profile,
                                                               'notifications':notifications,
                                                               'unseen_count':unseen_count})

def casher_dash(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request,'casher_dash/casher_dash.html',{'notifications':notifications,'unseen_count':unseen_count})
from datetime import datetime
from nurse_app.models import BedInformation,RoomInformation
def add_discharge(request):
    users = User.objects.all()
    payed = False
    
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        casher_name = request.POST.get('casher_name')
        discharge_date = request.POST.get('discharge_date')
        reffer = request.POST.get('reffere')
        status = request.POST.get('status')
        reason = request.POST.get('reason')
        
        try:
            patient = get_object_or_404(PatientRegister, patient_id=patient_id)
            p = get_object_or_404(BedInformation, Patient_id=patient_id)
            pt=p.Bed_no
            casher = get_object_or_404(User, username=casher_name)
            discharge_instance = Discharge(
                Patient_id=patient,
                Departure_date=discharge_date,
                Reason=reason,
                Casher_name=casher,
                Reffer_to=reffer,
                Status=status
            )
            
            # Calculate the number of days stayed
            bed_info = BedInformation.objects.filter(Patient_id=patient).first()
            if bed_info:
                alloc_date = bed_info.Alloc_date
                discharge_date = datetime.strptime(discharge_date, '%Y-%m-%d').date()
                discharge_instance.No_days = (discharge_date - alloc_date).days
            
            discharge_instance.save()
            bed = get_object_or_404(RoomInformation, Bed_no=pt)
            bed.Status = 'Vacant'  # Update status to 'Vacant' or any other value as needed
            bed.save()
        except PatientRegister.DoesNotExist:
            # Handle the case where the patient is not found
            # You can add appropriate error handling or redirect to an error page
            pass
        except User.DoesNotExist:
            # Handle the case where the casher is not found
            # You can add appropriate error handling or redirect to an error page
            pass
        
        payed = True
        return redirect("add-discharge")  # Redirect to the same page after saving
    
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    
    return render(request, 'casher_dash/add-discharge.html', {
        'users': users,
        'notifications': notifications,
        'unseen_count': unseen_count,
        'payed': payed  # Pass the 'payed' variable to the template
    })
def casher_dash_content(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request,'casher_dash/casher_dash_content.html',{'notifications':notifications,'unseen_count':unseen_count})
def dis_discharge(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    discharges = Discharge.objects.all()
    return render(request,'casher_dash/discharges.html',{'notifications':notifications,
                                                         'unseen_count':unseen_count,
                                                         'discharges':discharges})
@login_required
def approve_discharge_request(request, discharge_no):
    dis_request = get_object_or_404(Discharge, Discharge_no=discharge_no)
    dis_request.Approval = True
    dis_request.save()
    return redirect('approve_departure')
def add_payment(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    users = User.objects.all()
    payed=False
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        casher_name = request.POST.get('cashier_name')
        added_date = request.POST.get('adminssion_date')
        pay_no = request.POST.get('payment_no')
        f_payment = request.POST.get('food_payment')
        f_p_amount = float(request.POST.get('food_p_amount'))
        b_payment = request.POST.get('bed_payment')
        b_p_amount = float(request.POST.get('bed_p_amount'))
        c_payment = request.POST.get('card_payment')
        c_p_amount = float(request.POST.get('card_p_amount'))
        l_payment = request.POST.get('lab_payment')
        l_p_amount = float(request.POST.get('lab_p_amount'))
        other_payment = request.POST.get('other')
        other_p_amount = float(request.POST.get('other_amount'))
        payemnt_method = request.POST.get('payment_type')
        total =f_p_amount + b_p_amount +c_p_amount+l_p_amount+other_p_amount
     
        try:
            patient = get_object_or_404( PatientRegister,patient_id=patient_id)
            casher = get_object_or_404(User, username=casher_name)
            payment = PaymentModel.objects.create(
                Patient_id=patient,
                Pay_number=pay_no,
                Admit_date=added_date,
                Lab_payment=l_p_amount,
                Food_payment=f_p_amount,
                Service_payment=other_p_amount,
                Card_payment=c_p_amount,
                Bed_payment=b_p_amount,
                Pay_method=payemnt_method,
                Total=total,
                Casher_id=casher
            )
        except PatientRegister.DoesNotExist:
            # Handle the case where the patient is not found
            # You can add appropriate error handling or redirect to an error page
            pass
        except UserProfileInfo2.DoesNotExist:
            # Handle the case where the doctor is not found
            # You can add appropriate error handling or redirect to an error page
            pass
        payed=True
        return redirect("add-payment")
    payment = ServicePayment.objects.all()
    return render(request,'casher_dash/add-payment.html',{'payments':payment,
                                                          'payed':payed,
                                                          'users':users,
                                                          'notifications':notifications,
                                                            'unseen_count':unseen_count})
def about_payment(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request,'casher_dash/about-payment.html',{'notifications':notifications,
                                                            'unseen_count':unseen_count})
def dis_payment(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request,'casher_dash/payments.html',{'notifications':notifications,
                                                            'unseen_count':unseen_count})
def invoice(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request,'casher_dash/invoice.html',{'notifications':notifications,
                                                            'unseen_count':unseen_count})
#casher view end here.
