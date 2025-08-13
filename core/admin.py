from django.contrib import admin
from .models import Autores, Livros, Editoras, Revistas, Fotografos, Fotos, TrechoLivro, Referencias

# Registra os modelos para que apareçam na interface de admin
admin.site.register(Referencias)
admin.site.register(Autores)
admin.site.register(Livros)
admin.site.register(Editoras)
admin.site.register(TrechoLivro)
admin.site.register(Revistas)
admin.site.register(Fotografos)
admin.site.register(Fotos)