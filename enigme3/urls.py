from django.urls import path

from . import views

urlpatterns = [
    path("", views.ajouterJoueur, name="ajouterJoueur"),
    path("data/", views.tableauAffichage, name="tableauAffichage"),
    path("game/", views.game, name="game"),
]
