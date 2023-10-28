from django.shortcuts import render, get_object_or_404, get_list_or_404

from .forms import AddRecipeForm, UserCreationForm
from .models import Recipe, Author


def index(request):
    print(request)
    recipes = get_list_or_404(Recipe)
    recipe = recipes[0]
    print(recipes)
    context = {
        "title": recipe.name,
        "description": recipe.description,
        "ingredients": recipe.ingredients,
        "steps": recipe.steps,
        "duration": recipe.steps,
    }
    return render(request,
                  'cookbook/index.html',
                  context=context)


def add_recipe_form(request):
    title = "Add recipe"
    message = ""
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            steps = form.cleaned_data['steps']
            duration = form.cleaned_data['duration']
            ingredients = form.cleaned_data['ingredients']
            author_pk = form.cleaned_data['author_pk']
            author = get_object_or_404(Author, pk=author_pk)
            Recipe(
                name=name,
                description=description,
                steps=steps,
                duration=duration,
                ingredients=ingredients,
                author=author,
            ).save()
    else:
        message = "Add a recipe"
        form = AddRecipeForm()
    return render(request, 'cookbook/add_recipe.html',
                  {'form': form, 'title': title, 'message': message})


def all_recipes(request):
    pass


def one_recipe(request):
    pass
