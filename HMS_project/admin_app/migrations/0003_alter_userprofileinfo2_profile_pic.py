# Generated by Django 5.0.2 on 2024-03-04 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_rename_profession_userprofileinfo2_specialty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo2',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics/'),
        ),
    ]