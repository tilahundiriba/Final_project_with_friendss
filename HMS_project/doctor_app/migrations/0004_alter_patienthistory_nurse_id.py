# Generated by Django 5.0.2 on 2024-05-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0003_remove_appointment_time_slot_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patienthistory',
            name='Nurse_ID',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
