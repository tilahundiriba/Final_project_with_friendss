# Generated by Django 5.0.2 on 2024-04-13 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patienthistory',
            name='symptom2',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
