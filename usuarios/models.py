from django.db import models
from django.utils import timezone
from BD.models import Projeto
# Create your models here.
class Categoria (models.Model):
    nome = models.CharField(max_length=300)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField (max_length=300)
    sobrenome = models.CharField(max_length=300)
    telefone = models.CharField (max_length=300, blank=True)
    email = models.CharField (max_length=300,blank=True)
    formação = models.CharField (max_length=300,blank=True)
    função = models.CharField (max_length=300,blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True,  upload_to='fotos/%Y/%m')

    def __str__(self):
        return self.nome

