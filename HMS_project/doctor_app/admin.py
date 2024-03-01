from django.contrib import admin
from .models import PatientHistory,Prescription,Appointment,Laboratory
admin.site.register(PatientHistory)
admin.site.register(Prescription)
admin.site.register(Appointment)
admin.site.register(Laboratory)
