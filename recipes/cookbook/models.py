from django.db import models

# Create your models here.
# Подготовьте нижеперечисленные модели:
# + Рецепты:
# - Название
# - Описание
# - Шаги приготовления
# - Время приготовления
# - Изображение
# - Автор
# - *другие поля на ваш выбор, например ингредиенты и т.п.
#
# + *Категории рецептов
# - Название
# - *другие поля на ваш выбор
#
# + *Связующая таблица для связи Рецептов и Категории
# - *обязательные для связи поля
# - *другие поля на ваш выбор


class Author(models.Model):
    nickname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default="None")
    reg_date = models.DateTimeField(auto_now_add=True)


class Recipe(models.Model):
    name = models.CharField(max_length=100)             # - Название
    description = models.CharField(max_length=100)      # - Описание
    ingredients = models.CharField(max_length=2000, default="...")
    steps = models.TextField(max_length=2000)           # - Шаги приготовления
    duration = models.PositiveIntegerField()            # - Время приготовления
    image = models.ImageField(                          # - Изображение
        upload_to='images/', default=None, null=True)
    author: Author = models.ForeignKey(                 # - Автор
        Author, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=True)


# class Category(models.Model):
#     title
#
#
# class Relations(models.Model):
#     pass
