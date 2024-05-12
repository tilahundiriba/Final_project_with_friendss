from django.db import models
from receptionist_app.models import PatientRegister
from django.contrib.auth.models import User
class PatientHistory(models.Model):
    Patient_ID=models.ForeignKey(PatientRegister, on_delete=models.CASCADE)
    Date=models.DateField(auto_now_add=True)
    Sympthom=models.TextField(max_length=100)
    symptom2 = models.TextField(max_length=200 ,null=True)
    History_No=models.AutoField(primary_key=True)
    DiseaseName=models.TextField(max_length=100)
    Nurse_ID=models.ForeignKey(User,on_delete=models.CASCADE)
    Doctor_ID=models.ForeignKey(User,on_delete=models.CASCADE,related_name='nurse_history_set',related_query_name='doctor_history')
    Is_checked= models.BooleanField(default=False)
 
    def __str__(self):
        return f'{self.Patient_ID,self.Nurse_ID,self.Doctor_ID,self.DiseaseName}'

class Appointment(models.Model):
    PatientID=models.ForeignKey(PatientRegister, on_delete=models.CASCADE)
    App_number=models.BigAutoField(primary_key=True)
    App_date=models.DateField(auto_now_add=True)
    Appointment_date=models.DateField(null=True)
    Start_Time=models.TimeField(max_length=100,null=True)
    End_Time=models.TimeField(max_length=100,null=True)
    Doctor_ID=models.ForeignKey(User,on_delete=models.CASCADE)
    App_reason = models.TextField(max_length=200)
    App_status = models.TextField(max_length=100)


class Prescription(models.Model):
    PatientID=models.ForeignKey(PatientRegister, on_delete=models.CASCADE)
    Prec_number=models.BigAutoField(primary_key=True)
    Prec_date=models.DateField(auto_now_add=True)
    Precscriptions=models.TextField(max_length=200,null=True)
    Patient_full_name=models.TextField(max_length=100)
    Doctor_ID=models.ForeignKey(User,on_delete=models.CASCADE)

class Laboratory(models.Model):
    PatientID=models.ForeignKey(PatientRegister, on_delete=models.CASCADE)
    Lab_number=models.BigAutoField(primary_key=True)
    Admit_date=models.DateField(auto_now_add=True)
    Lab_type=models.TextField(max_length=200)
    Lab_result=models.TextField(max_length=100, null=True)
    Doctor_ID=models.ForeignKey(User,on_delete=models.CASCADE)
    Technician_ID=models.ForeignKey(User,on_delete=models.CASCADE,related_name='laboratory_send_set',related_query_name='laboratory_send_set',null=True)
    Is_tested= models.BooleanField(default=False)
    Is_payed= models.BooleanField(default=False)
    Is_prescriped= models.BooleanField(default=False)
    def __str__(self):
        return f'{self.PatientID}'