# Generated by Django 5.0.2 on 2024-05-09 08:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurse_app', '0001_initial'),
        ('receptionist_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('Room_no', models.TextField(primary_key=True, serialize=False)),
                ('Bed_no', models.TextField(max_length=100)),
                ('Room_type', models.CharField(max_length=100)),
                ('Status', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BedAllocation',
            fields=[
                ('Room_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Bed_num', models.TextField()),
                ('Room_type', models.CharField(max_length=100)),
                ('Alloc_date', models.DateField(auto_now_add=True)),
                ('Patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receptionist_app.patientregister')),
                ('Room_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nurse_app.rooms')),
            ],
        ),
    ]