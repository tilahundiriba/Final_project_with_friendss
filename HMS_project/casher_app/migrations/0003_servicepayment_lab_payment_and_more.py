# Generated by Django 5.0.2 on 2024-03-20 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casher_app', '0002_servicepayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepayment',
            name='Lab_payment',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='servicepayment',
            name='Bed_payment',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicepayment',
            name='Card_payment',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicepayment',
            name='Food_payment',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicepayment',
            name='Service_payment',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
