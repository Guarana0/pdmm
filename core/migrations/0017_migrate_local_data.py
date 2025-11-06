# Generated manually to handle data migration

from django.db import migrations, models
import django.db.models.deletion
from django.utils.text import slugify


def migrate_local_data(apps, schema_editor):
    """
    Migra os dados do campo local (CharField) para local_new (ForeignKey)
    """
    Fotos = apps.get_model('core', 'Fotos')
    Locais = apps.get_model('core', 'Locais')
    
    for foto in Fotos.objects.all():
        if foto.local:  # Se o campo local tem um valor
            try:
                # Buscar o objeto Local correspondente
                local_obj = Locais.objects.get(nome=foto.local)
                foto.local_new = local_obj
                foto.save()
            except Locais.DoesNotExist:
                # Se não encontrar, criar um novo Local
                local_obj = Locais.objects.create(
                    nome=foto.local,
                    slug=slugify(foto.local)
                )
                foto.local_new = local_obj
                foto.save()


def reverse_migrate_local_data(apps, schema_editor):
    """
    Reverte a migração copiando de volta de local_new para local
    """
    Fotos = apps.get_model('core', 'Fotos')
    
    for foto in Fotos.objects.all():
        if foto.local_new:
            foto.local = foto.local_new.nome
            foto.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_create_locais_model'),
    ]

    operations = [
        # Adicionar o novo campo ForeignKey temporário
        migrations.AddField(
            model_name='fotos',
            name='local_new',
            field=models.ForeignKey(blank=True, help_text='Local onde a foto foi tirada', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fotos_temp', to='core.locais'),
        ),
        # Migrar os dados
        migrations.RunPython(migrate_local_data, reverse_migrate_local_data),
    ]