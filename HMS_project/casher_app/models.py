from django.db import models
from receptionist_app.models import PatientRegister
from admin_app.models import UserProfileInfo2
from django.contrib.auth.models import User
from nurse_app.models import BedInformation
from datetime import datetime
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
class Discharge(models.Model):
    Discharge_no = models.AutoField(primary_key=True)
    Patient_id = models.ForeignKey(PatientRegister, on_delete=models.CASCADE)
    Reason = models.TextField(max_length=100, null=True)
    Departure_date = models.DateField(null=True)
    Status = models.TextField(max_length=100, null=True)
    No_days = models.BigIntegerField(null=True)
    Reffer_to = models.TextField(max_length=100, null=True)
    Approval = models.BooleanField(default=False)
    Casher_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # def save(self, *args, **kwargs):
    # # Calculate the number of days stayed before saving
    #     if self.Discharge_date:
    #         bed_info = BedInformation.objects.filter(Patient_id=self.Patient_id).first()
    #         if bed_info:
    #             alloc_date = bed_info.Alloc_date # Convert to datetime.date object
    #             discharge_date = self.Discharge_date
    #             if isinstance(discharge_date, str):
    #                 discharge_date = datetime.strptime(discharge_date, '%Y-%m-%d').date()
    #             self.No_days = (discharge_date - alloc_date).days
    #     super(Discharge, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.Patient_id}, {self.Discharge_no}, {self.Approval}'