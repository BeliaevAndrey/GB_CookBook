from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('add_recipe/', views.add_recipe_form, name='add_recipe_form'),
    path('stub/', views.stub, name='stub'),
]
