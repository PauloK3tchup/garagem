# Generated by Django 4.2.4 on 2023-08-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("uploader", "0001_initial"),
        ("garagem", "0003_remove_veiculo_imagem_veiculo_imagem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="veiculo",
            name="imagem",
            field=models.ManyToManyField(blank=True, default=None, related_name="+", to="uploader.image"),
        ),
    ]
