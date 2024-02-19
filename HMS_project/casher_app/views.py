from django.shortcuts import render

def casher_dash(request):
    return render(request,'casher_dash/casher_dash.html')
def casher_dash_content(request):
    return render(request,'casher_dash/casher_dash_content.html')
def dis_bill(request):
    return render(request,'casher_dash/bill.html')
def add_payment(request):
    return render(request,'casher_dash/add-payment.html')
def about_payment(request):
    return render(request,'casher_dash/about-payment.html')
def dis_payment(request):
    return render(request,'casher_dash/payments.html')
def invoice(request):
    return render(request,'casher_dash/invoice.html')
#casher view end here.
