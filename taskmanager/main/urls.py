from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about.html', views.about),
    path('menu.html', views.menu),
    path('lunch.html', views.lunch),
    path('starters.html', views.starters),
    path('sweets.html', views.sweets)
]
