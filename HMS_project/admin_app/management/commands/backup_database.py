# backup_database.py
import os
from django.core.management.base import BaseCommand
from django.conf import settings
import psycopg2

class Command(BaseCommand):
    help = 'Backup PostgreSQL database tables'

    def handle(self, *args, **kwargs):
        # PostgreSQL database configuration
        db_settings = settings.DATABASES['default']
        host = db_settings['HOST']
        port = db_settings['PORT']
        username = db_settings['USER']
        password = db_settings['PASSWORD']
        database = db_settings['NAME']

        # Backup directory
        backup_dir = os.path.join(settings.BASE_DIR, 'backups')
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Create a new PostgreSQL database connection
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            dbname=database
        )

        # Get a list of all tables in the database
        tables = []
        with conn.cursor() as cursor:
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
            for row in cursor.fetchall():
                tables.append(row[0])

            # Loop through each table and export its data
            for table in tables:
                filename = os.path.join(backup_dir, f'{table}.sql')
                with open(filename, 'w', encoding='utf-8') as f:
                    # Retrieve table data
                    cursor.execute(f'SELECT * FROM "{table}"')
                    for row in cursor.fetchall():
                        values = "','".join(str(value) for value in row)
                        f.write(f"INSERT INTO \"{table}\" VALUES ('{values}');\n")

        # Close the connection
        conn.close()

        self.stdout.write(self.style.SUCCESS('Backup completed successfully!'))
