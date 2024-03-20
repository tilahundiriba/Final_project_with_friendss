from django.shortcuts import render
from .models import PaymentModel
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
