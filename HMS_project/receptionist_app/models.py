from django.db import models
from admin_app.models import User
class PatientRegister(models.Model):
    patient_id = models.CharField(primary_key=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField()
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    kebele = models.CharField(max_length=200)
    staff=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.patient_id
class ppp(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)