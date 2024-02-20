from django.db import models

class RoomInformation(models.Model):
    Room_block=models.TextField(max_length=100)
    Room_no=models.TextField(max_length=100 ,primary_key=True)
    Bed_no=models.CharField(max_length=100)
    Status=models.TextField(max_length=100)
