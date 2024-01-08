from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
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