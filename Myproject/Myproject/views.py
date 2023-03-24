from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


def bemvindo(request):
    return HttpResponse(
        "<p style = 'color: red;'>Bem vindo ao curso de Django</p>")


def categoriaIdade(request, idade):
    if idade >= 18:
        if idade >= 60:
            categoria = "Terceira idade"
        else:
            categoria = "Adulto"
    else:
        if idade <= 10:
            categoria = "Infancia"
        else:
            categoria = "Adolecencia"
    resultado = "<h1> Categoria da Idade: %s</h1>" % categoria
    return HttpResponse(resultado)


def horarioAtual(request):
    resposta = "<h1>Data e Horário atual: {0}</h1>".format(
        # datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
        datetime.datetime.now().ctime())

    return HttpResponse(resposta)


def conteudoHTML(request, nome, idade):
    conteudo = """
    <html>
    <body>
    <p style = "font-weight:bold">Nome: %s / Idade %s</p>
    </body>
    </html>
    """ % (nome, idade)
    return HttpResponse(conteudo)


def primeiroTemplate(request):
    template = open(
        "C:/Users/Divisão de Extensão/Desktop/Learn_Django/Myproject/Myproject/templates/primeiro.html")
    templateT = Template(template.read())
    template.close()
    contexto = Context()
    documento = templateT.render(contexto)
    return HttpResponse(documento)


def telaParametros(request):
    nome = 'Reynan'
    data_atual = datetime.datetime.now()
    linguagens = ['Python', 'Ruby', 'Java', 'Dart', 'Javascript', 'C', 'Lua']
    template = open(
        "C:/Users/Divisão de Extensão/Desktop/Learn_Django/Myproject/Myproject/templates/telaParametros.html")
    templateT = Template(template.read())
    template.close()
    contexto = Context({"nome": nome, "data": data_atual, "linguagens": linguagens})
    documento = templateT.render(contexto)
    return HttpResponse(documento)


def telaCarregada(request): 
    nome = 'Reynan'
    data_atual = datetime.datetime.now()
    linguagens = [
        'Python', 'Ruby', 'Java', 'Dart',
        'Javascript', 'C', 'Lua', 'PHP'
        ]
    telaExterna = get_template('telaParametros.html')  # loader
    doc = telaExterna.render(
        {"nome": nome, "data": data_atual, "linguagens": linguagens})
    return HttpResponse(doc)


def telaEncurtada(request):
    nome = 'Reynan'
    data_atual = datetime.datetime.now()
    linguagens = [
        'Python', 'Ruby', 'Java', 'Dart',
        'Javascript', 'C', 'Lua', 'PHP', 'C++', 'egua',
    ]

    return render(request, 'telaParametros.html', {"nome": nome, "data": data_atual, "linguagens": linguagens})


def telaFilha1(request):
    return render(request, 'telaFilha_1.html', {})


def telaFilha2(request):
    return render(request, 'telaFilha_2.html', {})
