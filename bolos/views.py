from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .forms import ReceitaForm
from .models import Receita


def index(request):  
    mos = Receita.objects.all()
    return render (request, 'bolos/index.html', {'mos': mos})


def receita(request, id):
    rec = get_object_or_404(Receita, pk=id)
    return render(request, 'bolos/receita.html', {'rec': rec})


def form(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
       # else: return render(request, 'bolos/formulario.html', {'form': form})
    else:
        form = ReceitaForm()
    return render(request, 'bolos/formulario.html', {'form': form})
    