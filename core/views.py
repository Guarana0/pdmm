from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import Autores
from django.contrib.auth.views import PasswordChangeView
from .models import Livros
from django.conf import settings
from django.core.paginator import Paginator
from .models import Revistas
from .models import Noticias
from .models import Fotos


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
    
    # Pega todas as revistas ordenadas por ano de publicação (mais recentes primeiro)
    revistas_list = Revistas.objects.all().order_by('-ano_publicacao')
    
    # Define quantos itens por página
    paginator = Paginator(revistas_list, 4)  # 4 revistas por página (1 linha de 4 cards)
    
    # Pega o número da página da query string
    page = request.GET.get('page')
    revistas = paginator.get_page(page)
    
    return render(request, 'core/revistas/diarioDeMinas.html', {'revistas': revistas})

def leiteCriollo(request):
    return render(request, 'core/revistas/leiteCriollo.html')

def revistaVerde(request):
    
    # Pega todas as revistas ordenadas por ano de publicação (mais recentes primeiro)
    revistas_list = Revistas.objects.all().order_by('-ano_publicacao')
    
    # Define quantos itens por página
    paginator = Paginator(revistas_list, 8)  # 8 revistas por página (2 linhas de 4 cards)
    
    # Pega o número da página da query string
    page = request.GET.get('page')
    revistas = paginator.get_page(page)
    
    return render(request, 'core/revistas/revistaVerde.html', {'revistas': revistas})

def revista_detail(request, slug):
    revista = get_object_or_404(Revistas, slug=slug)
    
    # Busca a revista anterior baseado no ano de publicação e título
    revista_anterior = Revistas.objects.filter(
        ano_publicacao__gte=revista.ano_publicacao
    ).exclude(
        id_revista=revista.id_revista
    ).filter(
        ano_publicacao=revista.ano_publicacao,
        titulo__lt=revista.titulo
    ).order_by('-ano_publicacao', '-titulo').first()
    
    if not revista_anterior:
        revista_anterior = Revistas.objects.filter(
            ano_publicacao__lt=revista.ano_publicacao
        ).order_by('-ano_publicacao', '-titulo').first()
    
    # Busca a próxima revista baseado no ano de publicação e título
    revista_proxima = Revistas.objects.filter(
        ano_publicacao__lte=revista.ano_publicacao
    ).exclude(
        id_revista=revista.id_revista
    ).filter(
        ano_publicacao=revista.ano_publicacao,
        titulo__gt=revista.titulo
    ).order_by('ano_publicacao', 'titulo').first()
    
    if not revista_proxima:
        revista_proxima = Revistas.objects.filter(
            ano_publicacao__gt=revista.ano_publicacao
        ).order_by('ano_publicacao', 'titulo').first()
    
    context = {
        'revista': revista,
        'revista_anterior': revista_anterior,
        'revista_proxima': revista_proxima
    }
    
    return render(request, 'core/revista_detail.html', context)

def galeria(request):
    return render(request, 'core/galeria.html')

def livros(request):
    return render(request, 'core/livros.html')

def livros_detail(request, slug):
    livro = get_object_or_404(Livros, slug=slug)
    return render(request, 'core/livros_detail.html', {'livro': livro})

def noticia_detail(request, slug):
    noticia = get_object_or_404(Noticias, slug=slug)
    return render(request, 'core/noticia_detail.html', {'noticia': noticia})

def foto_detail(request, slug):
    foto = get_object_or_404(Fotos, slug=slug)
    return render(request, 'core/foto_detail.html', {'foto': foto})



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