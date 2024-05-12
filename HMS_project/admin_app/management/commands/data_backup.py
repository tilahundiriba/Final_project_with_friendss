from django.core.management.base import BaseCommand
from admin_app.tasks import backup_database

class Command(BaseCommand):
    help = 'Initiate backup process with specified interval'

    def handle(self, *args, **kwargs):
        interval_hours = 1  # Set the interval to 24 hours
        backup_database.apply_async((interval_hours,))
