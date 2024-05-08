from django.contrib import admin
from .models import RoomInformation,VitalInformation,Medication,BedInformation
# Register your models here.
admin.site.register(RoomInformation)
admin.site.register(VitalInformation)
admin.site.register(Medication)
admin.site.register(BedInformation)