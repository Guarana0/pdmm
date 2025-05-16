from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def autores(request):
    return render(request, 'core/autores.html')

def noticias(request):
    return render(request, 'core/noticias.html')

def revistas(request):
    return render(request, 'core/revistas.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def livros(request):
    return render(request, 'core/livros.html')