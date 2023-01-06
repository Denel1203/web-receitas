from django.shortcuts import render, redirect
from .forms import ReceitaForm


def index(request):  
    return render (request, 'bolos/index.html')


def receita(request):
    return render(request, 'bolos/receita.html')


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
    