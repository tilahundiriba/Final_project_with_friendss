from django.contrib import admin
from .models import LabTest,Payment ,UserProfile,BedAllocation,UserProfileInfo2
# Register your models here.
admin.site.register(LabTest)
admin.site.register(Payment)
admin.site.register(UserProfile)
admin.site.register(BedAllocation)
admin.site.register(UserProfileInfo2)

