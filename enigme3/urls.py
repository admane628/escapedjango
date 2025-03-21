from django.urls import path

from . import views

urlpatterns = [
    path("data/", views.tableauAffichage, name="tableauAffichage"),
    path("", views.home, name="home"),
]
