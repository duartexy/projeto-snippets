from rest_framework import serializers
from .models import Snippet

# Criamos o tradutor para o modelo Snippet
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        # fields = '__all__' diz para traduzir TODAS as colunas da tabela
        fields = '__all__'