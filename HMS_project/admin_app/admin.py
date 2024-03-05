from django.contrib import admin
from .models import LabTest,Payment ,UserProfile,BedAllocation,UserProfileInfo2
# Register your models here.
admin.site.register(LabTest)
admin.site.register(Payment)
admin.site.register(UserProfile)
admin.site.register(BedAllocation)
admin.site.register(UserProfileInfo2)

# 👇 1. Add this line import notification model
from .models import Notification

# 👇 2. Add this line to add the notification
admin.site.register(Notification)