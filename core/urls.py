from django.contrib import admin
from django.urls import path, include # Adicionamos o 'include' aqui!

urlpatterns = [
    path('admin/', admin.site.urls),
    # Adicionamos a rota principal da nossa API:
    path('api/', include('snippets.urls')), 
]