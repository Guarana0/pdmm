from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Create your models here.

# Tabela de autores
class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    data_falecimento = models.DateField(null=True, blank=True)
    local_nascimento = models.CharField(max_length=100, null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    
    # NOVO CAMPO DE IMAGEM
    # O primeiro argumento 'autores/' é o nome da pasta no Cloudinary onde as fotos serão salvas
    foto = CloudinaryField('autores/', null=True, blank=True)
    
    data_cadastro = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome + "-" + self.sobrenome)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    
    
# Tabela de Livros
class Livros(models.Model):
    id_livro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE, related_name='livros')
    genero = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    sinopse = models.TextField(null=True, blank=True)
    
    # CAMPO DE IMAGEM SUBSTITUINDO O URLField
    # As capas serão salvas na pasta 'livros/capas/' no Cloudinary
    capa = CloudinaryField('livros/capas/', null=True, blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

# Tabela de Editoras
class Editoras(models.Model):
    id_editora = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=255, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# Tabela de Revistas
class Revistas(models.Model):
    id_revista = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    editora = models.ForeignKey(Editoras, on_delete=models.CASCADE, related_name='revistas')
    edicao = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    capa_url = models.URLField(max_length=255, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

# Tabela de Fotógrafos
class Fotografos(models.Model):
    id_fotografo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    

# Tabela de Fotos
class Fotos(models.Model):
    id_foto = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=500)
    fotografo = models.ForeignKey(Fotografos, on_delete=models.CASCADE, related_name='fotos')
    local = models.CharField(max_length=200)

    data_cadastro = models.DateTimeField(auto_now_add=True)