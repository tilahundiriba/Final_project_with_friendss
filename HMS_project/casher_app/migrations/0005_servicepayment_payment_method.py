# Generated by Django 5.0.2 on 2024-03-21 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casher_app', '0004_rename_bed_payment_servicepayment_payment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepayment',
            name='Payment_method',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
