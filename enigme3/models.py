from django.db import models

class Joueur(models.Model) :
    id_joueur=models.AutoField(primary_key=True)
    nom = models.CharField(max_length=32)

    def __str__(self):
        return self.nom

class Ingredients(models.Model) :
    id_ingredient=models.AutoField(primary_key=True)
    nom_ingredient = models.CharField(max_length=255) ## answer
    formuleChimique=models.CharField(max_length=255)
    propriete = models.CharField(max_length=255) ## question

    def __str__(self):
        return self.nom_ingredient
