from django.shortcuts import (render,
                              HttpResponse,
                              HttpResponseRedirect)
from random import choices

from .forms import AddRecipeForm
from .models import Recipe
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'cookbook/index.html'

    def get_context_data(self, **kwargs):
        recipes = list(Recipe.objects.all())
        if not recipes:
            context = {'title': 'Случайные рецепты', 'message': 'Здесь пока ничего нет.'}
            return context
        if len(recipes) > 5:
            recipes = choices(recipes, k=5)
        context = {
            'title': 'Случайные рецепты',
            'recipes': recipes,
        }
        return context


class AllRecipes(TemplateView):
    template_name = 'cookbook/index.html'

    def get_context_data(self, **kwargs):
        recipes = list(Recipe.objects.all())
        if not recipes:
            context = {'title': 'Случайные рецепты', 'message': 'Здесь пока ничего нет.'}
            return context
        context = {
            'title': 'Случайные рецепты',
            'recipes': recipes,
        }
        return context


class AddRecipe(LoginRequiredMixin, TemplateView):
    template_name = 'cookbook/add_recipe.html'
    login_url = 'login'

    # def __init__(self, request, **kwargs):
    #     super().__init__(**kwargs)
    #     self.request = request

    def post(self, request, **kwargs):
        if request.method == 'POST':
            form = AddRecipeForm(self.request.POST)
            print("!!" * 500)
            print(f'DEBUG: {form.fields}')
            if form.is_valid():
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                steps = form.cleaned_data['steps']
                duration = form.cleaned_data['duration']
                ingredients = form.cleaned_data['ingredients']
                author = get_user_model().objects.get(pk=self.request.user.pk)
                Recipe(
                    name=name,
                    description=description,
                    steps=steps,
                    duration=duration,
                    ingredients=ingredients,
                    author=author,
                ).save()

        return HttpResponseRedirect('/index/')

    def get_context_data(self, **kwargs):
        title = 'Add recipe'
        message = "Add a recipe"
        form = AddRecipeForm()
        context = {'form': form, 'title': title, 'message': message}
        return context


# def index(request):
#     recipes = list(Recipe.objects.all())
#     if not recipes:
#         return render(request,
#                       'cookbook/index_empty.html')
#     if len(recipes) > 5:
#         choices(recipes, k=5)
#     context = {
#         'title': 'Случайные рецепты',
#         'recipes': recipes,
#     }
#     return render(request,
#                   'cookbook/index.html',
#                   context=context)
#
#
#
# @login_required(login_url='login')
# def add_recipe_form(request):
#     title = "Add recipe"
#     message = ""
#     if request.method == 'POST':
#         form = AddRecipeForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             description = form.cleaned_data['description']
#             steps = form.cleaned_data['steps']
#             duration = form.cleaned_data['duration']
#             ingredients = form.cleaned_data['ingredients']
#             author = get_user_model().objects.get(pk=request.user.pk)
#             Recipe(
#                 name=name,
#                 description=description,
#                 steps=steps,
#                 duration=duration,
#                 ingredients=ingredients,
#                 author=author,
#             ).save()
#     else:
#         message = "Add a recipe"
#         form = AddRecipeForm()
#     return render(request, 'cookbook/add_recipe.html',
#                   {'form': form, 'title': title, 'message': message})
#
#
# def all_recipes(request):
#     pass
#
#
# def one_recipe(request):
#     pass
