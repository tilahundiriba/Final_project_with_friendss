from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Backup database data from all apps to CSV file'

    def add_arguments(self, parser):
        parser.add_argument('--interval', type=int, default=24, help='Interval in hours for backup')

    def handle(self, *args, **kwargs):
        interval = kwargs['interval']
        self.stdout.write(self.style.SUCCESS(f'Starting periodic backup with interval {interval} hours'))
        # Your backup logic here
