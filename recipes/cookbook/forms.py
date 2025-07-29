from django import forms
from .models import Category, Recipe


class AddRecipeForm(forms.Form):
    """ Add a recipe to database """

    categories = [(ctg.pk, f'{ctg.title}') for ctg in Category.objects.all()]
    name = forms.CharField(max_length=80, widget=forms.Textarea(attrs={'class': 'recipe__name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'recipe__field'}), max_length=500)
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'class': 'recipe__field'}))
    steps = forms.CharField(widget=forms.Textarea(attrs={'class': 'recipe__field'}))
    duration = forms.IntegerField(min_value=1)
    category = forms.ChoiceField(choices=categories)

    image = forms.ImageField(required=False)

