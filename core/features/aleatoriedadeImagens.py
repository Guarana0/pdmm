import random
from django.conf import settings
from core.models import Livros
from core.models import Fotos
import os


def escolherImagensLivros():
    queryset = Livros.objects.exclude(capa__isnull=True).exclude(capa__exact='')

    imagens = []
    for livro in queryset:
        # Tenta obter a URL da capa de forma segura — alguns storages podem não expor .url
        try:
            src = livro.capa.url
        except Exception:
            # Se não houver url (ou ocorrer erro), tenta usar o valor bruto (caso seja uma string)
            src = getattr(livro, 'capa', None)

        if src:
            imagens.append(src)

    # Se houver 4 ou mais, retorna 4 aleatórias
    if len(imagens) >= 4:
        selecionadas = random.sample(imagens, 4)
    else:
        # Usa todas as disponíveis
        selecionadas = list(imagens)

    resultado = []
    for src in selecionadas:
        resultado.append({'type': 'image', 'src': src})

    # Preenche com placeholders até chegar em 4
    while len(resultado) < 4:
        resultado.append({'type': 'placeholder'})

    return resultado

def escolherImagensFotos():
    queryset = Fotos.objects.exclude(imagem__isnull=True).exclude(imagem__exact='')

    imagens = []
    for foto in queryset:
        # Tenta obter a URL da capa de forma segura — alguns storages podem não expor .url
        try:
            src = foto.imagem.url
        except Exception:
            # Se não houver url (ou ocorrer erro), tenta usar o valor bruto (caso seja uma string)
            src = getattr(foto, 'imagem', None)

        if src:
            imagens.append(src)

    # Se houver 4 ou mais, retorna 4 aleatórias
    if len(imagens) >= 4:
        selecionadas = random.sample(imagens, 4)
    else:
        # Usa todas as disponíveis
        selecionadas = list(imagens)

    resultado = []
    for src in selecionadas:
        resultado.append({'type': 'image', 'src': src})

    # Preenche com placeholders até chegar em 4
    while len(resultado) < 4:
        resultado.append({'type': 'placeholder'})

    return resultado
