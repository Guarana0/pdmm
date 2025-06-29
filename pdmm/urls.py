from django.contrib import admin
from django.urls import path, include
from core import views # ou a importação que você usou
from django.conf import settings
from django.conf.urls.static import static


# SOBRESCREVER A VIEW DE LOGIN DO ADMIN
admin.site.login = views.MyAdminLoginView.as_view()

urlpatterns = [
    # Acessa dos Admins
    path('admin/', admin.site.urls), # Esta linha agora usará sua view de login
    path("accounts/", include("django.contrib.auth.urls")),
    
    # Acesso geral da pagina
    path('', include('core.urls') views.home, name='home'),
    
     path('autores/', views.autores, name='autores'),
     path('autores/<slug:slug>/', views.autor_detail, name='autor_detail'),
    
    path('noticias/', views.noticias, name='noticias'),
    path('revistas/', views.revistas, name='revistas'),
    path('galeria/', views.galeria, name='galeria'),
    path('livros/', views.livros, name='livros'),
    # ... outras URLs ...
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)