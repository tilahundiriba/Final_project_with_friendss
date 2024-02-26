from django.db import models
from receptionist_app.models import PatientRegister
from admin_app.models import UserProfileInfo2
from django.contrib.auth.models import User
class RoomInformation(models.Model):
    Room_block=models.TextField(max_length=100)
    Room_no=models.TextField(max_length=100 ,primary_key=True)
    Bed_no=models.CharField(max_length=100)
    Status=models.TextField(max_length=100)

class VitalInformation(models.Model):
    Patient_id=models.ForeignKey(PatientRegister,on_delete=models.CASCADE,related_name='nurse_vitalinfo_set',related_query_name='nurse_vitalinfo_set')
    Vital_info_no=models.TextField(max_length=100 ,primary_key=True)
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
    D_record=models.DateField()
    Remark=models.TextField(max_length=100)
