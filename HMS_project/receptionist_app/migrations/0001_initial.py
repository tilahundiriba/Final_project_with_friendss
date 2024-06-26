# Generated by Django 5.0.2 on 2024-05-21 10:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientRegister',
            fields=[
                ('patient_id', models.TextField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.TextField(max_length=100)),
                ('middle_name', models.TextField(blank=True, max_length=100)),
                ('last_name', models.TextField(max_length=100)),
                ('gender', models.TextField(max_length=10)),
                ('birth_date', models.DateField()),
                ('age', models.DecimalField(decimal_places=1, max_digits=3)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('country', models.TextField(max_length=100)),
                ('city', models.TextField(max_length=100)),
                ('region', models.TextField(max_length=100)),
                ('kebele', models.TextField(max_length=200)),
                ('symptom', models.TextField(max_length=200, null=True)),
                ('is_checked', models.BooleanField(default=False)),
                ('is_card', models.BooleanField(default=False)),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_patients', to=settings.AUTH_USER_MODEL)),
                ('receptinist_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
