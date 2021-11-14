from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about.html', views.about),
    path('menu.html', views.menu),
    path('lunch.html', views.lunch),
    path('starters.html', views.starters),
    path('sweets.html', views.sweets),
    path('contact.html', views.contact),
    path('recipe.html', views.recipe),
    path('reservation.html', views.reservation),
    path('sexy_salmon.html', views.sexy_salmon),
    path('awesome_recipe.html', views.awesome_recipe)
]
