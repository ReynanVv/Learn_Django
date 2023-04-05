from django.urls import path
from Aplicacoes.Academico.views import CursoListView

urlpatterns = [
    path('', CursoListView.as_view(), name='pibex')
]
