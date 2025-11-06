from django.contrib import admin
from .models import Autores, Livros, Editoras, Noticias, Revistas, Fotografos, Fotos, TrechoLivro, Referencias, Locais
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Locais)
class LocaisAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'estado', 'get_fotos_count', 'data_cadastro')
    list_filter = ('estado', 'cidade')
    search_fields = ('nome', 'cidade', 'estado')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('nome',)
    change_form_template = 'admin/core/galeria/change_form.html'
    
@admin.register(Fotos)
class FotosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'local', 'ano', 'fotografo', 'data_cadastro')
    list_filter = ('local', 'ano', 'fotografo')
    search_fields = ('titulo', 'local__nome', 'descricao', 'fotografo__nome')
    prepopulated_fields = {'slug': ('titulo',)}
    ordering = ('-data_cadastro',)
    autocomplete_fields = ['local', 'fotografo']
    change_list_template = 'admin/core/galeria/change_list.html'
    change_form_template = 'admin/core/galeria/change_form.html'

@admin.register(Fotografos)
class FotografosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_cadastro')
    search_fields = ('nome',)
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('nome',)
    change_form_template = 'admin/core/galeria/change_form.html'


@admin.register(Noticias)
class NoticiasAdmin(SummernoteModelAdmin):
    summernote_fields = ('conteudo',)
    list_display = ('titulo', 'get_autor_nome', 'data_publicacao', 'publicada', 'destaque')
    list_filter = ('publicada', 'destaque', 'data_publicacao')
    search_fields = ('titulo', 'subtitulo', 'conteudo')
    prepopulated_fields = {'slug': ('titulo',)}
    ordering = ('-data_publicacao',)
    change_list_template = 'admin/core/noticias/change_list.html'
    change_form_template = 'admin/core/noticias/change_form.html'

# Registra os outros modelos
admin.site.register(Referencias)
admin.site.register(Autores)
admin.site.register(Livros)
admin.site.register(Editoras)
admin.site.register(TrechoLivro)
admin.site.register(Revistas)