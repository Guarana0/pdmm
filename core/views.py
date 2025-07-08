from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import Autores



class MyAdminLoginView(LoginView):
    template_name = 'admin/login.html'
    


def home(request):
    return render(request, 'core/home.html')

def autores(request):
    return render(request, 'core/autores.html')

def autor_detail(request, slug):
    autor = get_object_or_404(Autores, slug=slug)
    return render(request, 'core/autor_detail.html', {'autor': autor})

def noticias(request):
    return render(request, 'core/noticias.html')

def revistas(request):
    return render(request, 'core/revistas.html')

def diario_de_minas(request):
    return render(request, 'core/revistas/diarioDeMinas.html')

def leiteCriollo(request):
    return render(request, 'core/revistas/leiteCriollo.html')

def revistaVerde(request):
    return render(request, 'core/revistas/revistaVerde.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def livros(request):
    return render(request, 'core/livros.html')

def registro(request):
    return render(request, 'admin/registro.html')

def login_view(request):
    return render(request, 'admin/login.html')