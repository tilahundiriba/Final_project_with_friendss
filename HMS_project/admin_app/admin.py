from django.contrib import admin
from .models import UserProfile,UserProfileInfo
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserProfileInfo)

# 👇 1. Add this line import notification model
from .models import Notification

# 👇 2. Add this line to add the notification
admin.site.register(Notification)