# Generated by Django 5.0.2 on 2024-04-29 16:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('receptionist_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('Services', models.TextField(max_length=100)),
                ('Payment_method', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Discharge',
            fields=[
                ('Discharge_no', models.AutoField(primary_key=True, serialize=False)),
                ('Reason', models.TextField(max_length=100, null=True)),
                ('Departure_date', models.DateField(auto_now_add=True)),
                ('Status', models.TextField(max_length=100, null=True)),
                ('No_days', models.BigIntegerField(null=True)),
                ('Reffer_to', models.TextField(max_length=100, null=True)),
                ('Approval', models.BooleanField(default=False)),
                ('Casher_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receptionist_app.patientregister')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('Pay_number', models.AutoField(primary_key=True, serialize=False)),
                ('Admit_date', models.DateField(auto_now_add=True)),
                ('Lab_payment', models.DecimalField(decimal_places=2, max_digits=1000, null=True)),
                ('Food_payment', models.DecimalField(decimal_places=2, max_digits=1000, null=True)),
                ('Service_payment', models.DecimalField(decimal_places=2, max_digits=1000, null=True)),
                ('Card_payment', models.DecimalField(decimal_places=2, max_digits=1000, null=True)),
                ('Bed_payment', models.DecimalField(decimal_places=2, max_digits=1000, null=True)),
                ('Pay_method', models.TextField(max_length=100, null=True)),
                ('Total', models.DecimalField(decimal_places=2, max_digits=1000, null=True)),
                ('Casher_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='casher_send_set', related_query_name='casher_send_set', to=settings.AUTH_USER_MODEL)),
                ('Patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receptionist_app.patientregister')),
            ],
        ),
    ]
