import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DockerProject.settings")
import django
django.setup()

from Doject.models import Product

products_data = [
    {'name': 'Pilka'},
    {'name': 'Koszulka'},
]

for data in products_data:
    Product.objects.create(**data)