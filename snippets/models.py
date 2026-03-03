from django.db import models

class Snippet(models.Model):
    titulo = models.CharField(max_length=100)
    codigo = models.TextField()
    linguagem = models.CharField(max_length=50)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo