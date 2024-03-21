from django.contrib import admin
from .models import LabTest,Payment ,UserProfile
# Register your models here.
admin.site.register(LabTest)
admin.site.register(Payment)
admin.site.register(UserProfile)

