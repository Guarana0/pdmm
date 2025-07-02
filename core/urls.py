from django.urls import path
from . import views # Importa as views do seu próprio aplicativo 'core'

app_name = 'core' # Isso é opcional, mas boa prática para namespace de URLs

urlpatterns = [
    path('', views.home, name='home'),
    path('autores/', views.autores, name='autores'),
    path('autores/<slug:slug>/', views.autor_detail, name='autor_detail'),
    path('noticias/', views.noticias, name='noticias'),
    path('revistas/', views.revistas, name='revistas'),
    path('galeria/', views.galeria, name='galeria'),
    path('livros/', views.livros, name='livros'),
    # ... adicione outras URLs específicas do app 'core' aqui se tiver
]
