from django.db import models
from recipes.settings import AUTH_USER_MODEL


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    ingredients = models.CharField(max_length=2000, default="...")
    steps = models.TextField(max_length=2000)
    duration = models.PositiveIntegerField()
    image = models.ImageField(
        upload_to='images/', default=None, null=True, blank=True)
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name='cookbook',
        on_delete=models.CASCADE, )
    add_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        related_name='category',
        on_delete=models.DO_NOTHING,
        null=True
    )

    def __str__(self):
        return self.name
