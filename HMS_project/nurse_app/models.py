from django.db import models
from receptionist_app.models import PatientRegister
from django.contrib.auth.models import User

class RoomInformation(models.Model):
    Room_block=models.TextField(max_length=100)
    Room_no=models.TextField()
    Bed_no=models.BigIntegerField(primary_key=True)
    Room_type=models.CharField(max_length=100)
    Status=models.TextField(max_length=100)
    def __str__(self):
        return f" {self.Bed_no}"

class BedInformation(models.Model):
    Patient_id=models.ForeignKey(PatientRegister,on_delete=models.CASCADE)
    Room_num=models.TextField()
    Room_id=models.BigAutoField(primary_key=True)
    Bed_num=models.ForeignKey(RoomInformation,on_delete=models.CASCADE)
    Room_type=models.CharField(max_length=100)
    Alloc_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.Bed_num}"

class VitalInformation(models.Model):
    Patient_id=models.ForeignKey(PatientRegister,on_delete=models.CASCADE,related_name='nurse_vitalinfo_set',related_query_name='nurse_vitalinfo_set')
    Vital_info_no=models.BigAutoField(primary_key=True)
    H_rate=models.CharField(max_length=100)
    B_pressure=models.TextField(max_length=100)
    Body_temp=models.TextField(max_length=100)
    Pain_level=models.TextField(max_length=100)
    Weight=models.TextField(max_length=100)
    Height=models.TextField(max_length=100)
    Nurse_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Oxy_satu=models.TextField(max_length=100)
    B_gluc_level=models.TextField(max_length=100)
    R_rate=models.TextField(max_length=100)
    D_record=models.DateField(auto_now_add=True)
    Remark=models.TextField(max_length=100)

class Medication(models.Model):
    Patient_id=models.ForeignKey(PatientRegister,on_delete=models.CASCADE)
    Med_time=models.TimeField(auto_now_add=True)
    Bed_no=models.BigIntegerField()
    Remark=models.TextField(max_length=100)
    Nurse_name=models.ForeignKey(User,on_delete=models.CASCADE)
    Drugs=models.TextField(max_length=100)
    Med_no=models.BigAutoField(primary_key=True)

