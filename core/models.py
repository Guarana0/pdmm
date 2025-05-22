from django.db import models

# Create your models here.

class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    data_falecimento = models.DateField(null=True, blank=True)
    local_nascimento = models.CharField(max_length=100, null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    foto_url = models.URLField(max_length=255, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    
    

class Livros(models.Model):
    id_livro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE, related_name='livros')
    genero = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    sinopse = models.TextField(null=True, blank=True)
    capa_url = models.URLField(max_length=255, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Editoras(models.Model):
    id_editora = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=255, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
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