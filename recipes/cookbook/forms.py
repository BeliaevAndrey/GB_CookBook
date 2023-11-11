from django import forms


class AddRecipeForm(forms.Form):
    """ Add a recipe to data base """
    name = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'recipe__name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'recipe__field'}), max_length=500)
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'class': 'recipe__field'}))
    steps = forms.CharField(widget=forms.Textarea(attrs={'class': 'recipe__field'}))
    duration = forms.IntegerField(min_value=1)
