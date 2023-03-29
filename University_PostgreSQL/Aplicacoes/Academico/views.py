from django.shortcuts import render
from .models import Curso


def home(request):
    """busca todos os dados no bd e retorna os dados em forma de dicionario"""
    cursos = Curso.objects.all().order_by('nome')
    return render(request, "gestaoCursos.html", {"cursos": cursos})
