from django.urls import path
from . import views # Importa as views do seu próprio aplicativo 'core'

app_name = 'core' # Isso é opcional, mas boa prática para namespace de URLs

urlpatterns = [
    path('', views.home, name='home'),
    path('autores/', views.autores, name='autores'),
    path('autores/<slug:slug>/', views.autor_detail, name='autor_detail'),
    path('noticias/', views.noticias, name='noticias'),
    path('revistas/', views.revistas, name='revistas'),
    path('revistas/diarioDeMinas/', views.diario_de_minas, name='diario_de_minas'),
    path('revistas/leiteCriollo/', views.leiteCriollo, name='leiteCriollo'),
    path('revistas/revistaVerde/', views.revistaVerde, name='revistaVerde'),
    path('revistas/<slug:slug>/', views.revista_detail, name='revista_detail'),
    path('galeria/', views.galeria, name='galeria'),
    path('livros/', views.livros, name='livros'),
    path('livros/<slug:slug>/', views.livros_detail, name='livros_detail'),
    # ... adicione outras URLs específicas do app 'core' aqui se tiver
]
