from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SnippetViewSet

# 1. Criamos um "Roteador" automático
router = DefaultRouter()

# 2. Registramos o nosso Garçom no roteador com o nome 'snippets'
router.register(r'snippets', SnippetViewSet)

# 3. Criamos a lista de URLs que o Django vai ler
urlpatterns = [
    path('', include(router.urls)),
]