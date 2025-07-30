from django.shortcuts import (render,
                              HttpResponse,
                              HttpResponseRedirect,
                              get_object_or_404,
                              )
from random import sample

from .forms import AddRecipeForm
from .models import Recipe, Category
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, ListView, CreateView


class Index(TemplateView):
    template_name = 'cookbook/index.html'

    def get_context_data(self, **kwargs):
        recipes = list(Recipe.objects.all())
        if not recipes:
            context = {'title': 'Случайные рецепты', 'message': 'Здесь пока ничего нет.'}
            return context
        if len(recipes) > 5:
            recipes = sample(recipes, k=5)
        context = {
            'title': 'Случайные рецепты',
            'recipes': recipes,
        }
        return context


class AllRecipes(ListView):
    model = Recipe
    template_name = 'cookbook/all_recipes.html'
    context_object_name = 'recipes'
    paginate_by = 5
    ordering = "pk"
    extra_context = {"title": "Все рецепты"}


class Categories(TemplateView):
    template_name = 'cookbook/categories.html'

    def get_context_data(self, **kwargs):
        categories = [ctg for ctg in Category.objects.all()]
        recipes_by_category = {
            ctg.title: [recipe for recipe in Recipe.objects.all() if recipe.category == ctg]
            for ctg in categories
        }
        context = {
            "title": "Категории",
            "categories": recipes_by_category
        }

        return context


class AddRecipe(LoginRequiredMixin, TemplateView):
    form_class = AddRecipeForm
    template_name = 'cookbook/add_recipe.html'
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        categories = {f'{ctg.pk}': ctg for ctg in Category.objects.all()}
        if request.method == 'POST':
            form = AddRecipeForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                steps = form.cleaned_data['steps']
                duration = form.cleaned_data['duration']
                ingredients = form.cleaned_data['ingredients']
                category = categories[form.cleaned_data['category']]
                image = form.cleaned_data['image']
                author = get_user_model().objects.get(pk=self.request.user.pk)
                Recipe(
                    name=name,
                    description=description,
                    steps=steps,
                    duration=duration,
                    ingredients=ingredients,
                    author=author,
                    category=category,
                    image=image,
                ).save()
        return HttpResponseRedirect('/index/')


class RecipePage(DetailView):
    template_name = 'cookbook/recipe.html'

    def get(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe, pk=kwargs.get("pk"))
        steps = recipe.steps.split("\n")
        ingredients = recipe.ingredients.split("\n")
        context = {
            "recipe": recipe,
            "steps": steps,
            "ingredients": ingredients,
        }
        return render(request, self.template_name, context)
