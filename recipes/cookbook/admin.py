from django.contrib import admin
from .models import Category, Recipe

admin.site.register(Category)
admin.site.register(Recipe)


class CategoryAdmin(admin.ModelAdmin):
    ordering = ('title', 'description')
    list_filter = ('title',)
    search_fields = ('title',)
    readonly_fields = []

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title', 'description']
            }
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'fields': ['description']
            }
        )
    ]


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'author')
    ordering = ('name', 'category', 'author', 'add_date')
    list_filter = ('name', 'category')
    readonly_fields = ['author', 'add_date']

    fieldsets = [
        (
            None,
         {
             'classes': ['wide'],
             'fields': ['name', 'category', 'description', 'author']
         }
         ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'fields': [
                    'name',
                    'category',
                    'description',
                    'ingredients',
                    'steps',
                    'duration',
                    'image',
                    'author',
                    'add_date'
                ]
            }
        ),
    ]
