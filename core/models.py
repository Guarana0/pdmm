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