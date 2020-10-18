import csv
import csv
from django.core.management.base import BaseCommand
from squirrel_track.models import Squirrel

class Command(BaseCommand):
    help = 'import data from the 2018 census file'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file',help='file containing squirrel amount details')

    def handle(self, *args, **options):
        file_=options['squirrel_file']

        with open(file_) as fp:
            reader=csv.DictReader(fp)

            for item in reader:
                obj=Squirrel()
                obj.x=item['X']
                obj.y=item['Y']
                obj.Unique_Squirrel_ID=item['Unique Squirrel ID']
                obj.Shift=item['Shift']
                obj.Date=item['Date']
                obj.Age=item['Age']
                obj.save()



        msg = f'You are importing from{file_}'
        self.stdout.write(self.style.SUCCESS(msg))

