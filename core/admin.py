from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Autores, Livros, Editoras, Noticias, Revistas, Fotografos, Fotos, TrechoLivro, Referencias, Locais
from django_summernote.admin import SummernoteModelAdmin

# Unregister the default User admin
admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    change_list_template = 'admin/auth/user/change_list.html'
    change_form_template = 'admin/auth/user/change_form.html'

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
@admin.register(Referencias)
class ReferenciasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor_biografado', 'autor_referencia', 'tem_link', 'data_cadastro')
    list_filter = ('autor_biografado', 'tem_link')
    search_fields = ('titulo', 'autor_referencia', 'descricao')
    ordering = ('-data_cadastro',)
    change_list_template = 'admin/core/referencias/change_list.html'
    change_form_template = 'admin/core/referencias/change_form.html'
admin.site.register(Autores)
admin.site.register(Livros)
@admin.register(Editoras)
class EditorasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'localizacao', 'data_cadastro')
    search_fields = ('nome', 'localizacao')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('nome',)
    change_list_template = 'admin/core/editoras/change_list.html'
    change_form_template = 'admin/core/editoras/change_form.html'
@admin.register(TrechoLivro)
class TrechoLivroAdmin(admin.ModelAdmin):
    list_display = ('livro', 'ordem', 'data_cadastro')
    list_filter = ('livro',)
    search_fields = ('texto', 'livro__titulo')
    ordering = ('livro', 'ordem')
    change_list_template = 'admin/core/trecholivro/change_list.html'
    change_form_template = 'admin/core/trecholivro/change_form.html'
@admin.register(Revistas)
class RevistasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'edicao', 'ano_publicacao', 'data_cadastro')
    list_filter = ('titulo', 'ano_publicacao')
    search_fields = ('titulo', 'edicao')
    prepopulated_fields = {'slug': ('titulo', 'edicao')}
    ordering = ('-ano_publicacao', 'titulo')
    change_list_template = 'admin/core/revistas/change_list.html'
    change_form_template = 'admin/core/revistas/change_form.html'
