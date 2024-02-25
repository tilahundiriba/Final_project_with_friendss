from django.contrib import admin
from .models import PatientHistory,Prescription,Appointment
admin.site.register(PatientHistory)
admin.site.register(Prescription)
admin.site.register(Appointment)
