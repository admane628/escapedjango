import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from enigme3.forms import JoueurForm
from enigme3.models import *
from django.urls import reverse
from urllib.parse import urlencode
# Create your views here.

def ajouterJoueur(request):
	if request.method=="POST":
		form = JoueurForm(request.POST)

		if form.is_valid():
			joueur=form.save()
			
			url = reverse('game')
			params = {'nom': form.cleaned_data['nom']}
			full_url = f"{url}?{urlencode(params)}"
			
			return redirect(full_url)
	else:
		form =JoueurForm()

	return render(request, "enigme3/joueurFormulaire.html", {"form": form})


def tableauAffichage(request) :
	
	#### python manage.py loaddata enigme3/fixtures/ingredients.json
	
	
	# if not Ingredients.objects.exists():
		# Ingredients.objects.create(nom_ingredient='Vitamine C', formuleChimique='C6H8O6', propriete='Je suis un antioxydant puissant, souvent extrait d’agrumes')
		# Ingredients.objects.create(nom_ingredient='Acide Hyaluronique', formuleChimique='C14H21NO11', propriete='Je retiens l’humidité dans la peau comme une éponge')
		# Ingredients.objects.create(nom_ingredient='Beurre de karité', formuleChimique='Beurre', propriete='Je proviens d’une noix africaine et hydrate intensément')
		# Ingredients.objects.create(nom_ingredient='2', formuleChimique='Nombre', propriete='1+1')
		# Ingredients.objects.create(nom_ingredient='10', formuleChimique='Nombre', propriete='5*2')
		# Ingredients.objects.create(nom_ingredient='3.14', formuleChimique='Nombre', propriete='π')
		
	data = Ingredients.objects.all().values()
	data = list(data)
	
	ingrdts = []
	for i in data:
		ingrdts.append(i["nom_ingredient"])
	
	random.shuffle(data)
	return JsonResponse({"data": data, "ingredients": ingrdts})

def game(request):
	return render(request, "enigme3/index.html")
