# Generated by Django 5.0.2 on 2024-03-30 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casher_app', '0002_alter_paymentmodel_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmodel',
            name='Total',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
