# Generated by Django 4.2.6 on 2024-02-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptionist_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientregister',
            name='is_checked',
            field=models.BooleanField(default=False),
        ),
    ]