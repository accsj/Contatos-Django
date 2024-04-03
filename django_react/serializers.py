from rest_framework import serializers
from .models import Contato

class ContatoSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['nome'] = validated_data['nome'].lower()
        validated_data['email'] = validated_data['email'].lower()
        return Contato.objects.create(**validated_data)

    class Meta:
        model = Contato
        fields = ['id', 'nome', 'telefone', 'email']
