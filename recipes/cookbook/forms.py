from django import forms
from django.contrib.auth.forms import UserCreationForm


class AddRecipeForm(forms.Form):
    """ Add a recipe to data base """
    name = forms.CharField(max_length=100)             # - Название
    description = forms.CharField(max_length=500)      # - Описание
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    steps = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    duration = forms.IntegerField(min_value=1)

