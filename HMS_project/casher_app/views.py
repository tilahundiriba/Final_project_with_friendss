from django.shortcuts import render,redirect
from .models import PaymentModel
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
        return redirect('profile_show')
    
    user_profile, created = UserProfileInfo2.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        user_profile.profile_pic = profile_pic
        user_profile.save()
        return redirect('profile_show')
    
    return render(request, 'casher_dash/update_profile.html', {'user_id': user_id, 'user_profile': user_profile})

def casher_dash(request):
    return render(request,'casher_dash/casher_dash.html')
def casher_dash_content(request):
    return render(request,'casher_dash/casher_dash_content.html')
def dis_bill(request):
    return render(request,'casher_dash/bill.html')
def add_payment(request):
    # if request.method == 'POST':
    #     patient_id = request.POST.get('patient_name')
    #     lab_test_id = request.POST.get('lab_test_type')
    #     payment_amount = request.POST.get('payment_amount')

    #     lab_test = LabTest.objects.get(id=lab_test_id)
    #     payment = PaymentModel.objects.create(
    #         patient_id=patient_id,
    #         lab_test=lab_test,
    #         payment_amount=payment_amount
    #     )
    #     return HttpResponse("Payment processed successfully!")
    lab_tests = PaymentModel.objects.all()
    return render(request,'casher_dash/add-payment.html',{'lab':lab_tests})
def about_payment(request):
    return render(request,'casher_dash/about-payment.html')
def dis_payment(request):
    return render(request,'casher_dash/payments.html')
def invoice(request):
    return render(request,'casher_dash/invoice.html')
#casher view end here.
