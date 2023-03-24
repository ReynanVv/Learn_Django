"""Myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Myproject.views import bemvindo, categoriaIdade, horarioAtual
from Myproject.views import primeiroTemplate, telaParametros, conteudoHTML
from Myproject.views import telaCarregada, telaEncurtada, telaFilha1, telaFilha2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bemvindo/', bemvindo),
    path('categoriaIdade/<int:idade>', categoriaIdade),
    path('horarioAtual/', horarioAtual),
    path('conteudoHTML/<nome>/<int:idade>', conteudoHTML),
    path('primeiroTemplate/', primeiroTemplate),
    path('telaParametros/', telaParametros),
    path('telaCarregada/', telaCarregada),
    path('telaEncurtada/', telaEncurtada),
    path('telaFilha1/', telaFilha1),
    path('telaFilha2/', telaFilha2),
]
