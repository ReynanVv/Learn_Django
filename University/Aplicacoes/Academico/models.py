from django.db import models

# Create your models here.


class Curso(models.Model):
    nome = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
