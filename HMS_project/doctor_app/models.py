from django.db import models
from receptionist_app.models import Patient
from admin_app.models import UserProfileInfo2

class PatientHistory(models.Model):
    PatientID=models.ForeignKey(Patient, on_delete=models.CASCADE)
    Date=models.DateField()
    Sympthom=models.CharField(max_length=100)
    DiseaseName=models.CharField(max_length=100)
    Nurse_ID=models.ForeignKey(UserProfileInfo2,on_delete=models.CASCADE)
    Doctor_ID=models.ForeignKey(UserProfileInfo2,on_delete=models.CASCADE,related_name='nurse_history_set',related_query_name='doctor_history')
