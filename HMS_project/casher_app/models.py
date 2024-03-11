from django.db import models
from receptionist_app.models import PatientRegister
from admin_app.models import UserProfileInfo2
# Create your models here.
class PaymentModel(models.Model):
    Patient_id=models.ForeignKey(PatientRegister, on_delete=models.CASCADE)
    Pay_number=models.CharField(max_length=100)
    Admit_date=models.DateField(max_length=100)
    Lab_payment=models.TextField(max_length=200,null=True)
    Food_payment=models.TextField(max_length=100, null=True)
    Service_payment=models.TextField(max_length=100, null=True)
    Card_payment=models.TextField(max_length=100)
    Bed_payment=models.TextField(max_length=100, null=True)
    Pay_method=models.TextField(max_length=100, null=True)
    Total=models.TextField(max_length=100, null=True)
    Casher_id=models.ForeignKey(UserProfileInfo2,on_delete=models.CASCADE,related_name='casher_send_set',related_query_name='casher_send_set',null=True)

    def __str__(self):
        return f'{self.Patient_id}'