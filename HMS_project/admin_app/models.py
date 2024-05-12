
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 1. 👇 Add the following line
class Notification(models.Model):
    Name = models.TextField(max_length=100)  # Associate each notification with a user
    Message = models.TextField(max_length=500)
    Title = models.TextField(max_length=100)
    Timestamp = models.DateTimeField(auto_now_add=True)
    Seen = models.BooleanField(default=False)
class UserNotification(models.Model):
    Name = models.TextField(max_length=100)  # Associate each notification with a user
    Message = models.TextField(max_length=500)
    Title = models.TextField(max_length=100)
    Timestamp = models.DateTimeField(auto_now_add=True)
    Seen = models.BooleanField(default=False)

    def __str__(self):
        return self.Message
class Feedback(models.Model):
    Name = models.TextField(max_length=100,null=True)
    Email = models.EmailField(max_length=100,null=True)
    Feedback= models.TextField(max_length=500)
    Added_no = models.DateTimeField(auto_now_add=True)
    Is_seen = models.BooleanField(default=False)
class Report(models.Model):
    Name = models.TextField(max_length=100,null=True)
    Title = models.TextField(max_length=100,null=True)
    Report_file= models.FileField(upload_to='documents/', blank=True)
    Added_no = models.DateTimeField(auto_now_add=True)
    Report_no = models.AutoField(primary_key=True)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.TextField(max_length=100)  # Add profession field
    specialty = models.TextField(max_length=100)  # Add profession field
    password_changed = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profile_pics',default='default.jpg', blank=True)

    def __str__(self):
        return f'{self.user.username,self.user,self.profile_pic,self.user_id,self.role,self.specialty,self.password_changed}'


class UserProfile(AbstractUser):
    reset_key = models.CharField(max_length=100, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
def __str__(self):
    return f"{self.reset_key}"








