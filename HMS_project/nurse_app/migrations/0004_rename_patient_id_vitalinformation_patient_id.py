# Generated by Django 5.0.2 on 2024-02-26 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nurse_app', '0003_rename_patientid_vitalinformation_patient_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vitalinformation',
            old_name='Patient_ID',
            new_name='Patient_id',
        ),
    ]
