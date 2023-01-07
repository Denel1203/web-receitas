from django.db import models
from datetime import datetime

TYPOS = (
        ("NOTICIAS", "NOTICIAS"),
        ("BOLETOS", "BOLETOS"),
        ("CONSULTAS", "CONSULTAS"),
        ("EXAMES", "EXAMES")
    )


class Receita(models.Model):
    Nome_Receita = models.CharField(max_length=50, choices=TYPOS)
    Ingredientees = models.TextField(max_length=300)
    Preparo = models.CharField(max_length=50)
    Rendimento = models.CharField(max_length=50)
    Categoria = models.CharField(max_length=50)
    Por = models.CharField(max_length=50)
    Modo_preparo = models.TextField(max_length=500)
    Date_Receita = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.Nome_Receita
