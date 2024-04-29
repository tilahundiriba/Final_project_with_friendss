# Import necessary modules
import csv
from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'Backup database data from all apps to CSV file'

    def handle(self, *args, **kwargs):
        # Define the file path for the CSV backup
        csv_file_path = 'backup.csv'  # Specify the desired file path
        
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
                
        self.stdout.write(self.style.SUCCESS(f'Database data from all apps backed up to {csv_file_path}'))
