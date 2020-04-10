from django.core.management.base import BaseCommand, CommandError
from library.models import Author
from csv import reader

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
        count = 0
        if csv_name_file is not None and csv_name_file[0] is not None:
            with open(csv_name_file[0], encoding="utf8") as csv_file:
                csv_read = reader(csv_file)
                for row in csv_read:
                    print(f'Importing... {row[0]}')
                    author = Author(name=row[0])
                    author.save()           
                    count += 1 
            
        self.stdout.write(self.style.SUCCESS('Successfully import! Records imported "%s"' % count))