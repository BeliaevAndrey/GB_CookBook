from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"title": "Front Page"}
    return render(request, 'cookbook/index.html', context=context)
