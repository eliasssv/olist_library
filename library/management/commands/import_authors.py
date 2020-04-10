from django.core.management.base import BaseCommand, CommandError
from library.models import Author
from csv import reader
from django.db.utils import IntegrityError

class Command(BaseCommand):
    """
    Custom command for manage.py - Import Authors from a .csv file
    Example: py manage.py import_authors <csv_file_name.csv>
    @since 2020-04-09
    @author eliasssv
    """
    help = 'Import many authors from .csv file'

    def add_arguments(self, parser):
        """
        Add the single argument of the custom command: csv_name_file
        """
        parser.add_argument('csv_name_file', nargs='+', type=str)

    def handle(self, *args, **options):
        """
        Execute the import
        """
        csv_name_file = options['csv_name_file']
        count_saved = 0
        count_not_saved = 0
        count = 0
        if csv_name_file is not None and csv_name_file[0] is not None:
            with open(csv_name_file[0], encoding="utf8") as csv_file:
                csv_read = reader(csv_file)
                for row in csv_read:
                    # Jump the first row, the header "name"
                    if count > 0:
                        try:
                            print(f'Importing... {row[0]}')
                            author = Author(name=row[0])
                            author.save()           
                            count_saved += 1 
                        except IntegrityError:
                            print(f'The author "{row[0]}" already exists')
                            count_not_saved += 1
                    count += 1
            
        self.stdout.write(self.style.SUCCESS(f'Successfully import!\n   Records imported {count_saved}\n   Not imported {count_not_saved}'))