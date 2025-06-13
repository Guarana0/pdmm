from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


class MyAdminLoginView(LoginView):
    template_name = 'admin/login.html'
    #form_class = MyCustomAuthenticationForm

class MyAdminRegisterView(LoginView):
    template_name = 'admin/registro.html'


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

def registro(request):
    return render(request, 'admin/registro.html')

def login_view(request):
    return render(request, 'admin/login.html')