import random
from django.shortcuts import render
from django.http import JsonResponse
from enigme3.forms import JoueurForm
from enigme3.models import *

# Create your views here.

def ajouterJoueur(request):
	pass

def tableauAffichage(request) :
	if not Ingredients.objects.exists():
		Ingredients.objects.create(nom_ingredient='Vitamine C', formuleChimique='C6H8O6', propriete='Je suis un antioxydant puissant, souvent extrait d’agrumes')
		Ingredients.objects.create(nom_ingredient='Acide Hyaluronique', formuleChimique='C14H21NO11', propriete='Je retiens l’humidité dans la peau comme une éponge')
		Ingredients.objects.create(nom_ingredient='Beurre de karité', formuleChimique='Beurre', propriete='Je proviens d’une noix africaine et hydrate intensément')
		Ingredients.objects.create(nom_ingredient='2', formuleChimique='Nombre', propriete='1+1')
		Ingredients.objects.create(nom_ingredient='10', formuleChimique='Nombre', propriete='5*2')
		Ingredients.objects.create(nom_ingredient='3.14', formuleChimique='Nombre', propriete='π')
		
	data = Ingredients.objects.all().values()
	data = list(data)
	
	ingrdts = []
	for i in data:
		ingrdts.append(i["nom_ingredient"])
	
	random.shuffle(data)
	return JsonResponse({"data": data, "ingredients": ingrdts})

def home(request):
	return render(request, "enigme3/index.html")
