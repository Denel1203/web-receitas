from django.shortcuts import render


def test(request):  
    return render (request, 'bolos/teste.html')
