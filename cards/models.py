from django.db import models
from django.utils import timezone


# Create your models here.
class Edicao(models.Model):
    nome = models.CharField(max_length=1000)
    ano = models.IntegerField

    def __str__(self):
        return self.nome


class Cor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Tipo(models.Model):
    nome = models.CharField(max_length=1000)

    def __str__(self):
        return self.nome


class Raridade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Card(models.Model):
    nome = models.CharField(max_length=1000)
    nome_ingles = models.CharField(max_length=1000)
    valor = models.FloatField
    data_cadastro = models.DateTimeField(default=timezone.now)
    edicao = models.ForeignKey(Edicao, on_delete=models.DO_NOTHING)
    cor = models.ForeignKey(Cor, on_delete=models.DO_NOTHING)
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING)
    raridade = models.ForeignKey(Raridade, on_delete=models.DO_NOTHING)
