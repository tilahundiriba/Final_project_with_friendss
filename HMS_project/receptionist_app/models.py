from django.db import models
from admin_app.models import User

class PatientRegister(models.Model):
    patient_id = models.TextField(primary_key=True,max_length=100)
    first_name = models.TextField(max_length=100)
    middle_name = models.TextField(max_length=100, blank=True)
    last_name = models.TextField(max_length=100)
    gender = models.TextField(max_length=10)
    birth_date = models.DateField()
    age = models.DecimalField(max_digits=3, decimal_places=1)   
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    country = models.TextField(max_length=100)
    city = models.TextField(max_length=100)
    region = models.TextField(max_length=100)
    kebele = models.TextField(max_length=200)
    symptom = models.TextField(max_length=200 ,null=True)
    receptinist_name = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_patients')
    is_checked=models.BooleanField(default=False)
    is_card=models.BooleanField(default=False)
    
    def __str__(self):
        return self.patient_id
