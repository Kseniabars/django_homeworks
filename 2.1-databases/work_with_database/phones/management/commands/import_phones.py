import csv

from django.core.management.base import BaseCommand
from phones.models import Phone

from slugify import slugify


class Command(BaseCommand):
    help = 'Import phones from CSV'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        csv_file = options.get('csv_file', 'phones.csv')
        with open(csv_file, 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            name = phone.get('name', '').strip()
            price = float(phone.get('price', 0.00))
            image = phone.get('image', '').strip()
            release_date = phone.get('release_date', '')
            lte_exists = phone.get('lte_exists', '').lower() in ('true', '1', 'yes', 'да')
            slug = slugify(name)

            Phone.objects.create(
                name = name,
                slug = slug,
                price = price,
                image = image,
                release_date = release_date,
                lte_exists = lte_exists,
            )
            self.stdout.write(f' Added: {name}')




