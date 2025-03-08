from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('games/doodle/', views.doodle_game, name='doodle_game'),
    path('games/reaction/', views.reaction_game, name='reaction_game'),
    path('games/puzzle/', views.puzzle_game, name='puzzle_game'),
]
