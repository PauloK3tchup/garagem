from django.db import models

from garagem.models import Modelo, Acessorio, Cor
from uploader.models import Image


class Veiculo(models.Model):
    modelo = models.ForeignKey(
        Modelo, on_delete=models.PROTECT, related_name="veiculos"
    )
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0
    )
    descricao = models.TextField()
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    acessorios = models.ForeignKey(
        Acessorio, on_delete=models.PROTECT, related_name="veiculos"
    )
    imagem = models.ManyToManyField(
        Image,
        related_name="+",
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"Modelo: {self.modelo} - Ano: {self.ano} - Cor: {self.cor}"

    class Meta:
        verbose_name_plural = "veiculos"
        verbose_name = "veiculo"
