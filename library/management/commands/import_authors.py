from django.core.management.base import BaseCommand, CommandError
from library.models import Author

class Command(BaseCommand):
    help = 'Import many authors from .csv file'

    def add_arguments(self, parser):
        parser.add_argument('csv_name_file', nargs='+', type=str)

    def handle(self, *args, **options):
        csv_name_file = options['csv_name_file']
        if csv_name_file is not None:
            author = Author(name="teste" + str(csv_name_file))
            author.save()
            
        self.stdout.write(self.style.SUCCESS('Successfully import! Records imported "%s"' % 1))