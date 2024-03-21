from django.shortcuts import render,redirect
from .models import PaymentModel,ServicePayment
from django.shortcuts import get_object_or_404
from admin_app.models import UserProfileInfo2
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    user = request.user
    return render(request, 'casher_dash/profile.html', {'user': user})

@login_required
def profile_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.user != user:  # Ensure user can only update their own profile
        return redirect('show_casher_profile')
    
    user_profile, created = UserProfileInfo2.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        user_profile.profile_pic = profile_pic
        user_profile.save()
        return redirect('show_casher_profile')
    
    return render(request, 'casher_dash/update_profile.html', {'user_id': user_id, 'user_profile': user_profile})

def casher_dash(request):
    return render(request,'casher_dash/casher_dash.html')
def casher_dash_content(request):
    return render(request,'casher_dash/casher_dash_content.html')
def dis_bill(request):
    return render(request,'casher_dash/bill.html')
def add_payment(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        casher_id = request.POST.get('cashier_name')
        added_date = request.POST.get('adminssion_date')
        pay_no = request.POST.get('payment_no')
        f_payment = request.POST.get('food_payment')
        f_p_amount = request.POST.get('food_p_amount')
        b_payment = request.POST.get('bed_payment')
        b_p_amount = request.POST.get('bed_p_amount')
        c_payment = request.POST.get('card_payment')
        c_p_amount = request.POST.get('card_p_amount')
        l_payment = request.POST.get('lab_payment')
        l_p_amount = request.POST.get('lab_p_amount')
        other_payment = request.POST.get('other')
        other_p_amount = request.POST.get('other_amount')
        payemnt_method = request.POST.get('payment_type')
        total =f_p_amount + b_p_amount +c_p_amount+l_p_amount+other_p_amount
        food=f_payment + f_p_amount
        bed=b_payment + b_p_amount
        card=c_payment + c_p_amount
        lab=l_payment + l_p_amount
        other= other_payment + other_p_amount
        payment = PaymentModel.objects.create(
            patient_id=patient_id,
            Pay_number=pay_no,
            Admit_date=added_date,
            Lab_payment=lab,
            Food_payment=food,
            Service_payment=other,
            Card_payment=card,
            Bed_payment=bed,
            Pay_method=payemnt_method,
            Total=total,
            Casher_id=casher_id
        )
        return redirect("casher_dash")
    payment = ServicePayment.objects.all()
    return render(request,'casher_dash/add-payment.html',{'payments':payment})
def about_payment(request):
    return render(request,'casher_dash/about-payment.html')
def dis_payment(request):
    return render(request,'casher_dash/payments.html')
def invoice(request):
    return render(request,'casher_dash/invoice.html')
#casher view end here.
