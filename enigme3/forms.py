from django.forms import ModelForm

from enigme3.models import Joueur


class JoueurForm(ModelForm):
    class Meta :
        model= Joueur
        fields = ["nom"]
        labels= {
            "nom" : "Nom du joueur"
        }
