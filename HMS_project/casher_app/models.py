from django.db import models
from receptionist_app.models import PatientRegister
from admin_app.models import UserProfileInfo2
from django.contrib.auth.models import User
# Create your models here.
class PaymentModel(models.Model):
    Patient_id=models.ForeignKey(PatientRegister, on_delete=models.CASCADE)
    Pay_number=models.CharField(max_length=100)
    Admit_date=models.DateField(max_length=100)
    Lab_payment=models.DecimalField(max_digits=1000, decimal_places=2, null=True)
    Food_payment=models.DecimalField(max_digits=1000, decimal_places=2, null=True)
    Service_payment=models.DecimalField(max_digits=1000, decimal_places=2, null=True)
    Card_payment=models.DecimalField(max_digits=1000, decimal_places=2, null=True)
    Bed_payment=models.DecimalField(max_digits=1000, decimal_places=2, null=True)
    Pay_method=models.TextField(max_length=100, null=True)
    Total = models.DecimalField(max_digits=1000, decimal_places=2, null=True)
    Casher_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='casher_send_set',related_query_name='casher_send_set',null=True)

    def __str__(self):
        return f'{self.Patient_id , self.Total}'
    
class ServicePayment(models.Model):
    Payment=models.TextField(max_length=100, null=True)
    Services=models.TextField(max_length=100, null=True)
    Payment_method=models.TextField(max_length=100, null=True)
  
    def __str__(self):
        return f'{self.Payment,self.Services,self.Payment_method}'