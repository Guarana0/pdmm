from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import Autores
from django.contrib.auth.views import PasswordChangeView



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

class MyAdminPasswordChangeView(PasswordChangeView):
    """
    Custom view to handle the admin password change form.
    """
    # You must specify a template_name or override get_template_names()
    template_name = 'admin/password_change_form.html'  # Or your custom template path
    
    # You must specify a success_url
    success_url = reverse_lazy('admin:password_change_done')

    # You can add other customizations here if needed
    # For example, to pass extra context to the template:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add your custom context
        context['site_title'] = 'My Awesome Site' 
        return context