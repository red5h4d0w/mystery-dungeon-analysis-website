from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("card/", views.card_overview, name="card-overview"),
    path("card/<str:cardName>", views.cards, name="card-info"),
    path("data-reception", views.data_reception, name="data-reception"),
    path("game/", views.game_overview, name="game-overview"),
    path("game/<int:pk>", views.game, name="game-details")
]