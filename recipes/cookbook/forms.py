from django import forms
from django.contrib.auth.forms import UserCreationForm


class AddRecipeForm(forms.Form):
    """ Add a recipe to data base """
    name = forms.CharField(max_length=100)             # - Название
    description = forms.CharField(max_length=500)      # - Описание
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    steps = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    duration = forms.IntegerField(min_value=1)
    # author_pk = forms.ChoiceField(choices=authors)
    # author_pk = forms.ModelChoiceField(queryset=Author.objects.all())
    # author: Author = forms.ForeignKey(Author, on_delete=forms.CASCADE)
    # image = forms.ImageField(upload_to='images/', default=None, null=True)

