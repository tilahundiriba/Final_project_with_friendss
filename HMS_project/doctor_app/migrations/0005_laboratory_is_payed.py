# Generated by Django 5.0.2 on 2024-03-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0004_laboratory_is_tested'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratory',
            name='Is_payed',
            field=models.BooleanField(default=False),
        ),
    ]