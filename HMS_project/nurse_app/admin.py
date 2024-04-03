from django.contrib import admin
from .models import RoomInformation,VitalInformation,Medication
# Register your models here.
admin.site.register(RoomInformation)
admin.site.register(VitalInformation)
admin.site.register(Medication)