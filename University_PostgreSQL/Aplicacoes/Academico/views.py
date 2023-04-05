from django.shortcuts import render
from django.views.generic import ListView
from .models import Curso


def home(request):
    """busca todos os dados no bd e retorna os dados em forma de dicionario"""
    # cursos = Curso.objects.all().filter(creditos__gte=4).order_by('nome')
    # cursos = Curso.objects.all().filter(nome__startswith='L').order_by('nome')
    cursos = Curso.objects.all().order_by('nome')
    data = {
        'titulo': 'PIBEX',
        'cursos': cursos
    }
    # return render(request, "gestaoCursos.html", {"cursos": cursos})
    return render(request, "gestaoCursos.html", data)


class CursoListView(ListView):
    model = Curso
    template_name = 'gestaoCursos.html'

    def get_queryset(self):
        return Curso.objects.all().order_by('nome')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'PIBEX'
        # print(context)
        return context
