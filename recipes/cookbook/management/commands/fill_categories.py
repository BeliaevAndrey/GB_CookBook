from django.core.management.base import BaseCommand
from cookbook.models import Category


class Command(BaseCommand):
    help = "Fill categories"

    def handle(self, *args, **options):

        dishes = ['Первые блюда', 'Вторые блюда', 'Десерты',
                  'Мясные блюда', 'Овощные блюда',
                  'Выпечка', 'Напитки', ]

        for dish in dishes:
            Category(title=dish).save()
