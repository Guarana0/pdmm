from django.shortcuts import render
from django.contrib.auth.views import LoginView


class MyAdminLoginView(LoginView): # <--- ESTA É A CLASSE QUE ESTAMOS FALANDO!
    template_name = 'admin/login.html'
    #form_class = MyCustomAuthenticationForm # Se você criar um formulário de login personalizado

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