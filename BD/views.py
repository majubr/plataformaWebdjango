import csv
import datetime
import io
from typing import List

import chardet
import pandas
import xlwt
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt



from .models import Especie


# Create your views here.

def index(request):
    especies = Especie.objects.order_by('Especie')
    paginator = Paginator(especies, 20)
    page = request.GET.get('p')
    especies = paginator.get_page(page)
    return render(request, 'BD/index.html', {
        'especies': especies
    })


def ver_especie(request, especie_id):
    especie = get_object_or_404(Especie, id=especie_id)

    return render(request, 'BD/ver_especie.html', {
        'especie': especie
    })


def busca(request):
    termo = request.GET.get('termo')
    campos = 'especie'

    especies = Especie.objects.annotate(
        especie=campos
    ).filter(
        especie__icontains=termo
    )
    paginator = Paginator(especies, 20)
    page = request.GET.get('p')
    especies = paginator.get_page(page)
    return render(request, 'BD/busca.html', {
        'especies': especies
    })


@csrf_exempt
def data_upload(request):
    template = 'BD/data_upload.html'
    prompt = {
        'order': 'Order of the CSV'
    }
    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('windows-1251')

    io_string = io.StringIO(data_set)
    next(io_string)
    column: list[str]
    for column in csv.reader(io_string, delimiter=';', quotechar="|"):
        _, created = Especie.objects.update_or_create(

            Data=column[0],
            Ano=column[1],
            Estacao=column[2],
            Classe=column[3],
            Ordem=column[4],
            Familia=column[5],
            Genero=column[6],
            Especie=column[7],
            Nome_popular=column[8],
            Numero_registros=column[9],
            Metodologia=column[10],
            Ponto_amostral=column[11],
            Regiao=column[12],
            Latitude=column[13],
            Longitude=column[14],
            Altitude=column[15],
            Responsavel_tecnico=column[16],
            Projeto=column[17],
            Especialidade=column[18]
        )

    context = {}
    return render(request, template, context)


def export_csv(request):
    response: HttpResponse = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachnebt; filename = Dados' + \
                                      str(datetime.datetime()) + ".csv"
    writer = csv.writer(response)
    writer.writerow(['id', 'Data', 'Ano', 'Estação', 'Classe', 'Ordem', 'Familia',
                     'Genero', 'Especie', 'Nome_popular', 'Numero_registros', 'Metodologia', 'Ponto_amostral',
                     'Regiao', 'Latitude', 'Longitude', 'Altitude', 'Responsavel_tecnico', 'Projeto', 'Especialidade'])
    dados = Especie.objects.filter(owner=request.user)

    for dado in dados:
        writer.writerow(dado.id, dado.Data, dado.Ano, dado.Estacao, dado.Classe, dado.Ordem, dado.Familia,
                        dado.Genero, dado.Especie, dado.Nome_popular, dado.Numero_registros, dado.Metodologia,
                        dado.Ponto_amostral,
                        dado.Regiao, dado.Latitude, dado.Longitude, dado.Altitude, dado.Responsavel_tecnico,
                        dado.Projeto, dado.Especialidade)
    return response

def export_excel(request):
    response: HttpResponse = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachnebt; filename = dados' + \
                                      str(datetime.datetime()) + ".xls"
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Dados')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns =['id', 'Data', 'Ano', 'Estação', 'Classe', 'Ordem', 'Familia',
                     'Genero', 'Especie', 'Nome_popular', 'Numero_registros', 'Metodologia', 'Ponto_amostral',
                     'Regiao', 'Latitude', 'Longitude', 'Altitude', 'Responsavel_tecnico', 'Projeto', 'Especialidade']
    for col_num in range(len(columns)):
         ws.writer(row_num,col_num[col_num],font_style)

    rows = Especie.objects.filter(owner=request.user).values_list('id', 'Data', 'Ano', 'Estação', 'Classe', 'Ordem', 'Familia',
                     'Genero', 'Especie', 'Nome_popular', 'Numero_registros', 'Metodologia', 'Ponto_amostral',
                     'Regiao', 'Latitude', 'Longitude', 'Altitude', 'Responsavel_tecnico', 'Projeto', 'Especialidade'
    )

    for row in rows:
        row_num +=1

        for col_num in range(len(row)):
            for col_num in range(len(row)):
                ws.write(row_num,col_num, str(row[col_num]), font_style)
        wb.save(response)

        return response


def retorna_total_herpeto(request):
    total = Especie.objects.all()
    print(total)
    return HttpResponse ('teste')