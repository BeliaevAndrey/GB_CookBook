from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('all_recipes/', views.AllRecipes.as_view(), name='all_recipes'),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe_form'),
    path('view_recipe/<int:pk>', views.RecipePage.as_view(), name='view_recipe'),
]
