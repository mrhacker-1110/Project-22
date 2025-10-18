from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_player/', views.create_player, name='create_player'),
    path('play_game/', views.play_game, name='play_game'),
]
