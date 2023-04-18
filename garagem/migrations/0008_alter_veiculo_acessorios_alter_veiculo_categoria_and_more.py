# Generated by Django 4.1.7 on 2023-04-18 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0007_alter_acessorio_options_alter_cor_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='acessorios',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='garagem.acessorio'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='garagem.categoria'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='cor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='garagem.cor'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='garagem.marca'),
        ),
    ]