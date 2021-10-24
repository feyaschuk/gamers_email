import csv
from django.core.management.base import BaseCommand
from esp.models import Email

class Command(BaseCommand):

    MODEL_TABLE = {
        Email: r'static/email.csv',        
    } 

    def handle(self, *args, **kwargs):
        for model, table in self.MODEL_TABLE.items():
            with open(table, 'r', encoding='utf8') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    data = dict(row.items())
                    model(**data).save()

        self.stdout.write(self.style.SUCCESS('Your base is ready!'))
