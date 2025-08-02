from django.contrib import admin
from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
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
                'fields': ['name', 'category', 'author']
            }
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'fields': [
                    'description',
                    'ingredients',
                    'steps',
                    'duration',
                    'image',
                    'add_date'
                ]
            }
        ),
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
