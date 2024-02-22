# Generated by Django 4.2.6 on 2024-02-22 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('receptionist_app', '0001_initial'),
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prec_number', models.CharField(max_length=100)),
                ('Prec_date', models.DateField(max_length=100)),
                ('Precscriptions', models.TextField(max_length=200, null=True)),
                ('Patient_full_name', models.TextField(max_length=100)),
                ('Doctor_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.userprofileinfo2')),
                ('P_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receptionist_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Sympthom', models.CharField(max_length=100)),
                ('DiseaseName', models.CharField(max_length=100)),
                ('Doctor_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nurse_history_set', related_query_name='doctor_history', to='admin_app.userprofileinfo2')),
                ('Nurse_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.userprofileinfo2')),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receptionist_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('App_number', models.CharField()),
                ('App_date', models.DateField(max_length=100)),
                ('Time_slot', models.TextField(max_length=100)),
                ('App_reseon', models.TextField(max_length=200)),
                ('App_status', models.TextField(max_length=100)),
                ('Doctor_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.userprofileinfo2')),
                ('P_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receptionist_app.patient')),
            ],
        ),
    ]
