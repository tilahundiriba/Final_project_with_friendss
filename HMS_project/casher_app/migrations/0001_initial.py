# Generated by Django 5.0.2 on 2024-03-11 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_app', '0002_alter_userprofileinfo2_profile_pic'),
        ('receptionist_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pay_number', models.CharField(max_length=100)),
                ('Admit_date', models.DateField(max_length=100)),
                ('Lab_payment', models.TextField(max_length=200, null=True)),
                ('Food_payment', models.TextField(max_length=100, null=True)),
                ('Service_payment', models.TextField(max_length=100, null=True)),
                ('Card_payment', models.TextField(max_length=100)),
                ('Bed_payment', models.TextField(max_length=100, null=True)),
                ('Pay_method', models.TextField(max_length=100, null=True)),
                ('Total', models.TextField(max_length=100, null=True)),
                ('Casher_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='casher_send_set', related_query_name='casher_send_set', to='admin_app.userprofileinfo2')),
                ('Patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receptionist_app.patientregister')),
            ],
        ),
    ]
