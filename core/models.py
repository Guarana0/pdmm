from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    data_falecimento= models.DateField(null=True, blank=True)
    local_nascimento = models.CharField(max_length=100, null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    foto = CloudinaryField('autores/', null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)
    
    class Meta:
        ordering = ['nome', 'sobrenome']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.nome}-{self.sobrenome}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

    def get_absolute_url(self):
        return f"/autores/{self.slug}/"
    
class Referencias(models.Model):
    autor_biografado = models.ForeignKey(Autores, on_delete=models.CASCADE, related_name='referencias')
    titulo = models.CharField(max_length=255, help_text="Título da referência ou site")
    autor_referencia = models.CharField(max_length=200, null=True, blank=True, help_text="Nome do autor da referência")
    descricao = models.TextField(null=True, blank=True, help_text="Descrição opcional")
    tem_link = models.BooleanField(default=False, help_text="Marque se existe um link para a referência")
    link = models.URLField(null=True, blank=True, help_text="URL da referência (opcional)")
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_acesso = models.DateField(null=True, blank=True, help_text="Data de acesso ao site (para ABNT)")

    class Meta:
        ordering = ['-data_cadastro', 'titulo']
        verbose_name = 'Referência de Pesquisa'
        verbose_name_plural = 'Referências de Pesquisa'

    def __str__(self):
        return f"{self.titulo} ({'com link' if self.tem_link else 'sem link'})"

    def abnt_format(self):
        # Formatação ABNT para referências
        partes = []
        if self.autor_referencia:
            # Se o autor da referência tem vírgula, assume formato "SOBRENOME, Nome"
            if ',' in self.autor_referencia:
                partes.append(f"{self.autor_referencia}.")
            else:
                # Se não tem vírgula, assume formato "Nome Sobrenome"
                nomes = self.autor_referencia.strip().split()
                if len(nomes) > 1:
                    sobrenome = nomes[-1].upper()
                    nome = ' '.join(nomes[:-1])
                    partes.append(f"{sobrenome}, {nome}.")
                else:
                    partes.append(f"{self.autor_referencia.upper()}.")
        
        partes.append(f"**{self.titulo}**.")
        
        if self.tem_link and self.link:
            partes.append(f"Disponível em: <{self.link}>.")
            if self.data_acesso:
                meses = {
                    1: 'jan.', 2: 'fev.', 3: 'mar.', 4: 'abr.', 5: 'mai.', 6: 'jun.',
                    7: 'jul.', 8: 'ago.', 9: 'set.', 10: 'out.', 11: 'nov.', 12: 'dez.'
                }
                mes = meses.get(self.data_acesso.month, str(self.data_acesso.month))
                partes.append(f"Acesso em: {self.data_acesso.day} {mes} {self.data_acesso.year}.")
            else:
                partes.append("Acesso em: [data de acesso].")
        
        return ' '.join(partes)

class Livros(models.Model):
    GENERO_CHOICES = [
        ('CONTO', 'Contos'),
        ('ROMANCE', 'Romance'),
        ('POESIA', 'Poesia'),
        ('CRONICA', 'Crônica'),
        ('ENSAIO', 'Ensaio'),
        ('OUTRO', 'Outro'),
    ]

    id_livro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE, related_name='livros')
    genero = models.CharField(max_length=100, choices=GENERO_CHOICES)
    ano_publicacao = models.IntegerField()
    sinopse = models.TextField(null=True, blank=True)
    capa = CloudinaryField('livros/', null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)
    editora = models.ForeignKey('Editoras', on_delete=models.SET_NULL, null=True, blank=True, related_name='livros')

    class Meta:
        ordering = ['-ano_publicacao', 'titulo']
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return f"/livros/{self.slug}/"
    
class TrechoLivro(models.Model):
    livro = models.ForeignKey('Livros', on_delete=models.CASCADE, related_name='trechos')
    texto = models.TextField(help_text="Trecho selecionado do livro")
    ordem = models.PositiveIntegerField(default=0, help_text="Ordem do trecho no livro (opcional)")
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordem', 'id']
        verbose_name = 'Trecho do Livro'
        verbose_name_plural = 'Trechos dos Livros'

    def __str__(self):
        return f"Trecho de {self.livro.titulo} (#{self.ordem})"

class Editoras(models.Model):
    id_editora = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=255, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Revistas(models.Model):
    id_revista = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    editora = models.ForeignKey(Editoras, on_delete=models.CASCADE, related_name='revistas')
    edicao = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    capa = CloudinaryField('revistas/', null=True, blank=True)  # Substituído URLField por CloudinaryField
    pdf = CloudinaryField('revistas/pdfs/', null=True, blank=True, resource_type='raw')  # Add this line
    data_cadastro = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)

    class Meta:
        ordering = ['-ano_publicacao', 'titulo']
        verbose_name = 'Revista'
        verbose_name_plural = 'Revistas'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.titulo}-{self.edicao}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.titulo} - {self.edicao}"

class Fotografos(models.Model):
    id_fotografo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Fotógrafo'
        verbose_name_plural = 'Fotógrafos'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Fotos(models.Model):
    id_foto = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=500)
    fotografo = models.ForeignKey(Fotografos, on_delete=models.CASCADE, related_name='fotos')
    local = models.CharField(max_length=200)
    imagem = CloudinaryField('fotos/', null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(null=True, blank=True)
    ano = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)

    class Meta:
        ordering = ['-ano', 'titulo']
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300, null=True, blank=True, help_text="Subtítulo ou descrição breve da notícia")
    conteudo = models.TextField()
    autor = models.ForeignKey(Autores, on_delete=models.SET_NULL, null=True, blank=True, related_name='noticias')
    autor_nome = models.CharField(max_length=100, null=True, blank=True, help_text="Nome do autor se não for um autor cadastrado")
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem_capa = CloudinaryField('noticias/', null=True, blank=True)
    imagem_capa_legenda = models.CharField(max_length=200, null=True, blank=True, help_text="Legenda da imagem de capa")
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)
    publicada = models.BooleanField(default=True, help_text="Define se a notícia está publicada")
    destaque = models.BooleanField(default=False, help_text="Define se a notícia aparece em destaque")
    
    class Meta:
        ordering = ['-data_publicacao', 'titulo']
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return f"/noticias/{self.slug}/"
    
    def get_autor_nome(self):
        """Retorna o nome do autor, seja ele cadastrado ou não"""
        if self.autor:
            return f"{self.autor.nome} {self.autor.sobrenome}"
        return self.autor_nome or "Equipe Editorial"

class ImagemNoticia(models.Model):
    noticia = models.ForeignKey(Noticias, on_delete=models.CASCADE, related_name='imagens_extras')
    imagem = CloudinaryField('noticias/extras/', null=True, blank=True)
    legenda = models.CharField(max_length=200, null=True, blank=True)
    ordem = models.PositiveIntegerField(default=0, help_text="Ordem de exibição da imagem na notícia")
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordem', 'id']
        verbose_name = 'Imagem da Notícia'
        verbose_name_plural = 'Imagens das Notícias'

    def __str__(self):
        return f"Imagem de {self.noticia.titulo} (#{self.ordem})"