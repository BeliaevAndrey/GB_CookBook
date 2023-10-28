from django.shortcuts import render


def index(request):
    print("index called")
    context = {"title": "Front Page"}
    return render(request,
                  'cookbook/index.html',
                  context=context)


def add_recipe(request):
    pass


def all_recipes(request):
    pass


def one_recipe(request):
    pass
