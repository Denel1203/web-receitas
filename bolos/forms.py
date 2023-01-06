from django.forms import ModelForm
from .models import Receita

# Create the form class.
class ReceitaForm(ModelForm):
    class Meta:
        model = Receita
        fields = ['Nome_Receita', 'Ingredientees', 'Preparo', 'Rendimento', 'Categoria', 'Por', 'Modo_preparo']