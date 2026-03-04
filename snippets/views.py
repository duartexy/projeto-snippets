from rest_framework import viewsets
from .models import Snippet
from .serializers import SnippetSerializer

# Criamos o nosso "Garçom" que vai gerenciar os Snippets
class SnippetViewSet(viewsets.ModelViewSet):
    # 1. Onde ele vai buscar os dados? (Na tabela Snippet inteira)
    queryset = Snippet.objects.all()
    
    # 2. Qual tradutor ele vai usar para entregar os dados?
    serializer_class = SnippetSerializer