from django.db import models
from django.http import HttpResponseRedirect


# Create your models here.
class Especialidade (models.Model):
    nome = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

class Projeto (models.Model):
    nome = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

class ID_sp(models.Model):
    objects = None
    Especie = models.CharField(max_length=50,default=True)

class ID_familia(models.Model):
    objects = None
    Familia = models.CharField(max_length=50,default=True)

class Especie(models.Model):
    objects = None
    Data = models.CharField (max_length=300, blank=True)
    Ano = models.IntegerField (blank=True)
    Estacao = models.CharField (max_length=300, blank=True)
    Classe = models.CharField (max_length=300,blank=True)
    Ordem = models.CharField (max_length=300,blank=True)
    Familia = models.CharField (max_length=300,blank=True)
    Genero = models.CharField (max_length=300,blank=True)
    Especie = models.CharField (max_length=300,blank=True)
    Nome_popular = models.CharField(max_length=300, blank=True)
    Numero_registros = models.IntegerField (blank=True)
    Metodologia = models.CharField (max_length=300,blank=True)
    Ponto_amostral = models.CharField(max_length=300, blank=True)
    Regiao = models.CharField(max_length=300, blank=True)
    Latitude = models.IntegerField (blank=True)
    Longitude = models.IntegerField (blank=True)
    Altitude = models.IntegerField(blank=True)
    Responsavel_tecnico = models.CharField(max_length=300)
    Projeto = models.CharField(max_length=300)
    Especialidade =models.CharField(max_length=300)





