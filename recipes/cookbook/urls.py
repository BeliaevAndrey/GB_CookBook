from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('all_recipes/', views.AllRecipes.as_view(), name='all_recipes'),
    # path('index/', views.Index.as_view(), name='index'),
    # path('', views.index, name='index'),
    # path('index/', views.index, name='index'),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe_form'),
    # path('add_recipe/', views.add_recipe_form, name='add_recipe_form'),
]
