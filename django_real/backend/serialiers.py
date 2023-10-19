from rest_framework import serializers
from .models import Client,Compte
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields=['id','code_cli','nom','prenom']
class CompteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Compte
        fields=['id','code_cpt','code_cli','d_cpt','solde']

