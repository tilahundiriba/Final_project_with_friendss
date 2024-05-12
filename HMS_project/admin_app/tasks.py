from celery import shared_task
from datetime import timedelta
from django.utils import timezone
import csv
from django.apps import apps

@shared_task
def backup_database(interval):
    # Define the file path for the CSV backup
    csv_file_path = 'admin_app/backup.csv'  # Specify the desired file path
    
    # Open the CSV file in write mode
    with open(csv_file_path, 'w', newline='') as csvfile:
        # Define the CSV writer
        writer = csv.writer(csvfile)
        
        # Iterate over all installed apps
        for app_config in apps.get_app_configs():
            # Iterate over all models in the app
            for model in app_config.get_models():
                # Get the data from the model
                queryset = model.objects.all()
                
                # Write the header row with the field names
                writer.writerow([field.name for field in model._meta.fields])
                
                # Write the data rows
                for obj in queryset:
                    writer.writerow([getattr(obj, field.name) for field in model._meta.fields])
    
    # Schedule next backup
    schedule_next_backup.apply_async((interval,), countdown=interval * 3600)  # Convert hours to seconds


@shared_task
def schedule_next_backup(interval):
    # Schedule the next backup
    next_backup_time = timezone.now() + timedelta(hours=interval)
    backup_database.apply_async((interval,), eta=next_backup_time)
