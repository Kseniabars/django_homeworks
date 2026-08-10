from django.core.management.base import BaseCommand
from books.models import Book
import json

class Command(BaseCommand):
    help = 'Import books '

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        json_file = options.get('json_file', 'fixtures/books.json')
        with open(json_file, 'r') as file:
            books = json.load(file)

        for item in books:
            fields = item.get('fields', {})

            name = fields.get('name', '').strip()
            author = fields.get('author', '').strip()
            pub_date = fields.get('pub_date', '').strip()

            if Book.objects.filter(name=name, author=author).exists():
                self.stdout.write(f'⏭️ Skipped: {name} (already exists)')
                continue

            Book.objects.create(
                name = name,
                author = author,
                pub_date = pub_date,
            )
            self.stdout.write(f' Added: {name}')
