# # tasks.py

# from celery import shared_task
# from django.utils import timezone
# from twilio.rest import Client
# from .models import Appointment
# from twilio.rest import Client
# from django.http import HttpResponse
# from datetime import datetime, timedelta
# from twilio.base.exceptions import TwilioRestException
# @shared_task
# def send_notification():
#     # Get appointments scheduled one hour from now
#     one_hour_from_now = timezone.now() + timezone.timedelta(hours=1)
#     appointments = Appointment.objects.filter(Time_slot=one_hour_from_now)

#     # Send notifications for each appointment
#     for appointment in appointments:
#         send_sms(appointment.PatientRegister.phone_number)

# def send_sms(phone_number):
#     # Twilio credentials
#    account_sid = 'AC853cc8d20b814ed3b23041aab29acec4'
#    auth_token = 'f3d400b45cf9e9a461e3cd14ad51716c'
#    twilio_number = '+19474652604'


#     # Initialize Twilio client
#    client = Client(account_sid, auth_token)

#     # Compose SMS message
#    message_body = "Your appointment is scheduled in one hour. Please be prepared."
    
#    try:
#         # Send SMS
#         message = client.messages.create(
#             body=message_body,
#             from_=twilio_number,
#             to=phone_number
#         )
#    except Exception as e:
#         print(f"Error sending SMS: {e}")
