from django.db import models
from django.utils.html import format_html

# Create your models here.


class Curso(models.Model):
    nome = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        texto = "{0} ({1})"
        return texto.format(self.nome, self.creditos)

    def cor(self):
        return format_html('<span style="text-transform: uppercase; font-weight: bold">{0}</span>'.format(self.nome))
    cor.short_description = 'Cursos'
