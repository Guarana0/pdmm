# Generated manually to handle data migration

from django.db import migrations, models
import django.db.models.deletion
from django.utils.text import slugify


def create_locais_from_existing_data(apps, schema_editor):
    """
    Cria registros de Locais baseados nos valores únicos existentes no campo local das Fotos
    """
    Fotos = apps.get_model('core', 'Fotos')
    Locais = apps.get_model('core', 'Locais')
    
    # Obter todos os locais únicos das fotos existentes
    locais_existentes = Fotos.objects.values_list('local', flat=True).distinct()
    
    for local_nome in locais_existentes:
        if local_nome:  # Só criar se não for vazio/null
            # Verificar se já existe
            if not Locais.objects.filter(nome=local_nome).exists():
                Locais.objects.create(
                    nome=local_nome,
                    slug=slugify(local_nome)
                )


def reverse_create_locais(apps, schema_editor):
    """
    Remove todos os registros de Locais criados
    """
    Locais = apps.get_model('core', 'Locais')
    Locais.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_fotos_fotografo'),
    ]

    operations = [
        # Criar o modelo Locais
        migrations.CreateModel(
            name='Locais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do local (ex: Belo Horizonte, Praça da Liberdade)', max_length=200, unique=True)),
                ('descricao', models.TextField(blank=True, help_text='Descrição do local', null=True)),
                ('cidade', models.CharField(blank=True, help_text='Cidade', max_length=100, null=True)),
                ('estado', models.CharField(blank=True, help_text='Estado', max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locais',
                'ordering': ['nome'],
            },
        ),
        # Adicionar campo fotografo
        migrations.AddField(
            model_name='fotos',
            name='fotografo',
            field=models.ForeignKey(blank=True, help_text='Fotógrafo responsável pela foto', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fotos', to='core.fotografos'),
        ),
        # Adicionar campo local_detalhes
        migrations.AddField(
            model_name='fotos',
            name='local_detalhes',
            field=models.CharField(blank=True, help_text="Detalhes específicos do local (ex: 'sala principal', 'fachada')", max_length=200, null=True),
        ),
        # Migração de dados para criar os Locais
        migrations.RunPython(create_locais_from_existing_data, reverse_create_locais),
    ]