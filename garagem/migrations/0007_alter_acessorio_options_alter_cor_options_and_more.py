# Generated by Django 4.1.7 on 2023-04-18 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0006_alter_veiculo_acessorios_alter_veiculo_categoria_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acessorio',
            options={'verbose_name': 'acessorio', 'verbose_name_plural': 'acessorios'},
        ),
        migrations.AlterModelOptions(
            name='cor',
            options={'verbose_name': 'cor', 'verbose_name_plural': 'cores'},
        ),
        migrations.AlterModelOptions(
            name='veiculo',
            options={'verbose_name': 'veiculo', 'verbose_name_plural': 'veiculos'},
        ),
    ]
