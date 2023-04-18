from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome.upper()


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name_plural = "cores"
        verbose_name = "cor"

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = "acessorios"
        verbose_name = "acessorio"
    
    
class Veiculo(models.Model):
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    descricao = models.TextField()
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name="veiculos"
        )
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name="veiculos"
        )
    acessorios = models.ForeignKey(
        Acessorio, on_delete=models.PROTECT, related_name="veiculos"
        )

    def __str__(self):
        return  f"Modelo: {self.modelo} - Marca: {self.marca.nome.upper()} - Ano: {self.ano} - Cor: {self.cor}"

    class Meta:
        verbose_name_plural = "veiculos"
        verbose_name = "veiculo"