
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 1. 👇 Add the following line
class Notification(models.Model):
    message = models.CharField(max_length=100)
    
    def __str__(self):
        return self.message

class UserProfileInfo2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100,null=True)  # Add profession field
    specialty = models.CharField(max_length=100)  # Add profession field
    password_changed = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return f'{self.user.username,self.user,self.profile_pic,self.user_id}'

class LabTest(models.Model):
    test_type = models.CharField(max_length=255)
    test_fee = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
      return f"{self.test_type}{self.test_fee}"
    
class Payment(models.Model):
    patient_name = models.CharField(max_length=255)
    lab_test = models.ForeignKey(LabTest, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
      return f"{self.patient_name}{self.lab_test} {self.payment_amount}"
    
  


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


# models.py
from django.db import models
from django.utils import timezone

class BedAllocation(models.Model):
    patient_id = models.IntegerField()
    alloc_date = models.DateField(default=timezone.now)
    departure_date = models.DateField(null=True, blank=True)

    def count_days_stayed(self):
        if self.departure_date:
            days_stayed = (self.departure_date - self.alloc_date).days
            return days_stayed
        else:
            # If departure date is not set, return None or handle it as needed
            return 0







