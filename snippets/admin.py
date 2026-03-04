from django.contrib import admin
from .models import Snippet

# Registrando o nosso modelo no painel de administração
admin.site.register(Snippet)