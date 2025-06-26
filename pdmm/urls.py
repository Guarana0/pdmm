from django.contrib import admin
from django.urls import path, include
from core import views # ou a importação que você usou

# SOBRESCREVER A VIEW DE LOGIN DO ADMIN
admin.site.login = views.MyAdminLoginView.as_view()

urlpatterns = [
    path('admin/', admin.site.urls), # Esta linha agora usará sua view de login
    path('registro/', views.registro),
    path('login/', views.login_view),
    path('', include('views.urls')),
    path('autores/', views.autores, name='autores'),
    path('noticias/', views.noticias, name='noticias'),
    path('revistas/', views.revistas, name='revistas'),
    path('galeria/', views.galeria, name='galeria'),
    path('livros/', views.livros, name='livros'),
    # ... outras URLs ...
]
