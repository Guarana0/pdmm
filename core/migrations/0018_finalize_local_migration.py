# Generated manually to handle data migration

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_migrate_local_data'),
    ]

    operations = [
        # Remover o campo local antigo (CharField)
        migrations.RemoveField(
            model_name='fotos',
            name='local',
        ),
        # Renomear local_new para local
        migrations.RenameField(
            model_name='fotos',
            old_name='local_new',
            new_name='local',
        ),
        # Atualizar o related_name para o valor correto
        migrations.AlterField(
            model_name='fotos',
            name='local',
            field=models.ForeignKey(help_text='Local onde a foto foi tirada', on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='core.locais'),
        ),
    ]