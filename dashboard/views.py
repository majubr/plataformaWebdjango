from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from BD.models import Especie,ID_sp
from usuarios.models import Contato
from django.db.models import Sum


def index(request):
    return render(request, 'dashboard/index.html')


def relatorio_total_herpeto(request):
    total = Especie.objects.all().aggregate(Sum('Numero_registros'))['Numero_registros__sum']
    print(total)
    return JsonResponse ({'Total de registros':total})


def relatorio_herpeto(request):
    dados = ID_sp.objects.all()
    print(dados)

    label = []
    data = []
    for dado in dados:
        especies = Especie.objects.filter(Especie=dado).aggregate(Sum('Numero_registros'))
        if not especies['Numero_registros__sum']:
            especies['Numero_registros__sum'] = 0
        label.append(dado.Especie)
        data.append(especies['Numero_registros__sum'])
        print(especies)

    x = list(zip(label, data))

    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))

    return JsonResponse({'labels': x[0][:], 'data': x[1][:]})