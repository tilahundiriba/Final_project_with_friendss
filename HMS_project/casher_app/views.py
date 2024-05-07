from django.shortcuts import render,redirect
from .models import PaymentModel,ServicePayment,Discharge
from django.shortcuts import get_object_or_404
from admin_app.models import UserProfileInfo,Notification
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from receptionist_app.models import PatientRegister
from django.core.paginator import Paginator
from doctor_app.models import Laboratory
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
    
    user_profile, created = UserProfileInfo.objects.get_or_create(user=user)
    
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
    card_payment=PatientRegister.objects.filter(is_card=False).count()
    lab_payment=Laboratory.objects.filter(Is_payed=False).count()
    # card_payment=PatientRegister.objects.filter(is_card=False)
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request,'casher_dash/casher_dash.html',{'notifications':notifications,
                                                          'unseen_count':unseen_count,
                                                          'card_payment':card_payment,
                                                          'lab_payment':lab_payment})
from datetime import datetime
from nurse_app.models import BedInformation,RoomInformation
def add_discharge(request):
    cashers = User.objects.filter(userprofileinfo__role='casher')
    payed = False
    
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        casher_name = request.POST.get('casher_name')
        reffer = request.POST.get('reffere')
        status = request.POST.get('status')
        reason = request.POST.get('reason')
        
        try:
            patient = get_object_or_404(PatientRegister, patient_id=patient_id)
            p = get_object_or_404(BedInformation, Patient_id=patient_id)
            pt=p.Bed_num
            casher = get_object_or_404(User, username=casher_name)
            discharge_instance = Discharge(
                Patient_id=patient,
                Reason=reason,
                Casher_name=casher,
                Reffer_to=reffer,
                Status=status
            )
            discharge_instance.save()
            # Calculate the number of days stayed
            bed_info = BedInformation.objects.filter(Patient_id=patient).first()
            date = get_object_or_404(Discharge, Patient_id=patient_id)
            if bed_info:
                alloc_date = bed_info.Alloc_date
                discharge_date = date.Departure_date
                discharge_instance.No_days = (discharge_date - alloc_date).days
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
        'cashers': cashers,
        'notifications': notifications,
        'unseen_count': unseen_count,
        'payed': payed  # Pass the 'payed' variable to the template
    })
def casher_dash_content(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    card_payment=PatientRegister.objects.filter(is_card=False).count()
    lab_payment=Laboratory.objects.filter(Is_payed=False).count()
    return render(request,'casher_dash/casher_dash_content.html',{'notifications':notifications,
                                                                  'unseen_count':unseen_count,
                                                                  'card_payment':card_payment,
                                                                  'lab_payment':lab_payment})
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
def add_payment(request,patient_id):
    notifications = Notification.objects.all()
    patient_pay = get_object_or_404(PatientRegister, patient_id=patient_id)
    unseen_count = Notification.objects.filter(seen=False).count()
    cashers = User.objects.filter(userprofileinfo__role='casher')
    for_card = get_object_or_404(ServicePayment, id=1)
    for_blood = get_object_or_404(ServicePayment, id=2)
    for_urine = get_object_or_404(ServicePayment, id=3)
    for_xray = get_object_or_404(ServicePayment, id=4)
    for_ctscan = get_object_or_404(ServicePayment, id=5)

    payed = False
    if request.method == 'POST':
        patientid = request.POST.get('patient_id')
        casher_name = request.POST.get('cashier_name')
        payment_method = request.POST.get('payment_type')
        blood_p_amount = request.POST.get('blood_test') == 'on'
        urine_p_amount = request.POST.get('urine_test') == 'on'
        ctscan_p_amount = request.POST.get('ctscan_test') == 'on'
        x_ray_test = request.POST.get('x-ray_test') == 'on'
        f_p_amount = request.POST.get('food_payment') == 'on'
        b_p_amount = request.POST.get('bed_payment') == 'on'
        c_p_amount = request.POST.get('card_payment') == 'on'
        
        # Initialize variables
        f_p = b_p = c_p = bl_p = ur_p = ct_p = xr_p = 0
        
        if f_p_amount:
            f_p = float(for_card.Payment)
        if b_p_amount:
            b_p = float(for_card.Payment)
        if c_p_amount:
            c_p = float(for_card.Payment)
        if blood_p_amount:
            bl_p = float(for_blood.Payment)
        if urine_p_amount:
            ur_p = float(for_urine.Payment)
        if ctscan_p_amount:
            ct_p = float(for_ctscan.Payment)
        if x_ray_test:
            xr_p = float(for_xray.Payment)
        
        lab_payment = bl_p + ur_p + ct_p + xr_p
        total = f_p + b_p + c_p + bl_p + ur_p + ct_p + xr_p
        try:
            patient = get_object_or_404(PatientRegister, patient_id=patientid)
            casher = get_object_or_404(User, username=casher_name)
            payment = PaymentModel.objects.create(
                Patient_id=patient,
                Lab_payment=lab_payment,
                Food_payment=f_p,
                Service_payment=lab_payment,
                Card_payment=c_p,
                Bed_payment=b_p,
                Pay_method=payment_method,
                Total=total,
                Casher_id=casher
            )
            patient_pay.is_card=True
            patient_pay.save()
        except PatientRegister.DoesNotExist:
            # Handle the case where the patient is not found
            # You can add appropriate error handling or redirect to an error page
            pass
        except User.DoesNotExist:
            # Handle the case where the cashier is not found
            # You can add appropriate error handling or redirect to an error page
            pass
        payed = True
        return redirect("dis_payment")
    payment = ServicePayment.objects.values('Payment_method').distinct()
    return render(request, 'casher_dash/add-payment.html', {'payments': payment,
                                                            'payed': payed,
                                                            'cashers': cashers,
                                                            'patient_pay': patient_pay,
                                                            'notifications': notifications,
                                                            'unseen_count': unseen_count})

def about_payment(request,pay_number,patient_id):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    payments = get_object_or_404(PaymentModel, Pay_number=pay_number)
    patients = get_object_or_404(PatientRegister, patient_id=patient_id)
    return render(request,'casher_dash/about-payment.html',{'notifications':notifications,
                                                            'unseen_count':unseen_count,
                                                            'payments':payments,
                                                            'patients':patients})
def dis_payment(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    payments = PaymentModel.objects.all()
    return render(request,'casher_dash/payments.html',{'notifications':notifications,
                                                            'unseen_count':unseen_count,
                                                            'payments':payments})
def invoice(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request,'casher_dash/invoice.html',{'notifications':notifications,
                                                            'unseen_count':unseen_count})


def add_payment_for_patient(request, patient_id):
    # Assuming you have a Payment model with fields like patient_id, card_payment, lab_payment, bed_payment, food_payment, etc.
    for_food = get_object_or_404(ServicePayment, id=6)
    for_bed = get_object_or_404(ServicePayment, id=7)
    # # Retrieve the most recent payment entry for the patient
    cashers = User.objects.filter(userprofileinfo__role='casher')
    payment = ServicePayment.objects.values('Payment_method').distinct()
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    recent_payment = PaymentModel.objects.filter(Patient_id=patient_id).latest('Admit_date')
    if recent_payment.Bed_payment and recent_payment.Food_payment == 0.00:
        recent_payment.Bed_payment = recent_payment.Food_payment = 1.0
        food_pay= recent_payment.Bed_payment * for_food.Payment
        bed_pay = recent_payment.Food_payment * for_bed.Payment
    else:
        food_pay= recent_payment.Bed_payment * for_food.Payment
        bed_pay = recent_payment.Food_payment * for_bed.Payment
    # # Add new payments to the existing payment entry
    # recent_payment.Bed_payment += new_bed_payment_amount
    # recent_payment.Food_payment += new_food_payment_amount

    # # Save the updated payment entry
    # recent_payment.save()

    # Redirect to a relevant page
    # return redirect('patient_detail', patient_id=patient_id)
    return render(request,'casher_dash/departure_payment.html',{'recent_payment':recent_payment,
                                                                'food_pay':food_pay,
                                                                'bed_pay':bed_pay,
                                                                'cashers':cashers,
                                                                'payment':payment,
                                                                'notifications':notifications,
                                                                'unseen_count':unseen_count})

def card_payments(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    card_payments = PatientRegister.objects.filter(is_card=False)
    paginator = Paginator(card_payments, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'casher_dash/card_payments.html',{'notifications':notifications,
                                                            'unseen_count':unseen_count,
                                                            'page_obj':page_obj})
#casher view end here.
