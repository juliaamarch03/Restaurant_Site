from django.shortcuts import render
from .models import Menu


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def menu(request):
    dinner = Menu.objects.filter(category='Вечеря')
    return render(request, 'main/menu.html', {'dinner': dinner})


def lunch(request):
    lunch = Menu.objects.filter(category='Обід')
    return render(request, 'main/lunch.html', {'lunch': lunch})


def starters(request):
    starters = Menu.objects.filter(category='Закуски')
    return render(request, 'main/starters.html', {'starters': starters})


def sweets(request):
    sweets = Menu.objects.filter(category='Солодощі')
    return render(request, 'main/sweets.html', {'sweets': sweets})


def contact(request):
    return render(request, 'main/contact.html')


def recipe(request):
    return render(request, 'main/recipe.html')


