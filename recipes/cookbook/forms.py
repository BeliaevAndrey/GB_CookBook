from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Author


class AddRecipeForm(forms.Form):
    """ Add a recipe to data base """
    authors = [(f'{author.pk}', f'{author.firstname} {author.last_name}')
               for author in Author.objects.all()]
    name = forms.CharField(max_length=100)             # - Название
    description = forms.CharField(max_length=500)      # - Описание
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    steps = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    duration = forms.IntegerField(min_value=1)
    author_pk = forms.ChoiceField(choices=authors)
    # author_pk = forms.ModelChoiceField(queryset=Author.objects.all())
    # author: Author = forms.ForeignKey(Author, on_delete=forms.CASCADE)
    # image = forms.ImageField(upload_to='images/', default=None, null=True)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    nickname = forms.CharField(max_length=100)
    firstname = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
