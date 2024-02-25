from django.db import models
from receptionist_app.models import PatientRegister
from admin_app.models import UserProfileInfo2

class PatientHistory(models.Model):
    Patient_ID=models.ForeignKey(PatientRegister, on_delete=models.CASCADE)
    Date=models.DateField()
    Sympthom=models.CharField(max_length=100)
    DiseaseName=models.CharField(max_length=100)
    Nurse_ID=models.ForeignKey(UserProfileInfo2,on_delete=models.CASCADE)
    Doctor_ID=models.ForeignKey(UserProfileInfo2,on_delete=models.CASCADE,related_name='nurse_history_set',related_query_name='doctor_history')


class Appointment(models.Model):
    PatientID=models.ForeignKey(PatientRegister, on_delete=models.CASCADE)
    App_number=models.CharField(max_length=100)
    App_date=models.DateField(max_length=100)
    Time_slot=models.TextField(max_length=100)
    Doctor_ID=models.ForeignKey(UserProfileInfo2,on_delete=models.CASCADE)
    App_reseon = models.TextField(max_length=200)
    App_status = models.TextField(max_length=100)


class Prescription(models.Model):
    PatientID=models.ForeignKey(PatientRegister, on_delete=models.CASCADE)
    Prec_number=models.CharField(max_length=100)
    Prec_date=models.DateField(max_length=100)
    Precscriptions=models.TextField(max_length=200,null=True)
    Patient_full_name=models.TextField(max_length=100)
    Doctor_ID=models.ForeignKey(UserProfileInfo2,on_delete=models.CASCADE)
  