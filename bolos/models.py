from django.db import models


class Receita(models.Model):
    Nome_Receita = models.CharField(max_length=50)
    Ingredientees = models.TextField(max_length=300)
    Preparo = models.CharField(max_length=50)
    Rendimento = models.CharField(max_length=50)
    Categoria = models.CharField(max_length=50)
    Por = models.CharField(max_length=50)
    Modo_preparo = models.TextField(max_length=500)
