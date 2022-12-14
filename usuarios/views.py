from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat
from .models import Contato
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    contatos = Contato.objects.order_by('nome').filter(
        mostrar=True
    )
    paginator = Paginator(contatos,20)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request,'usuarios/index.html',{
        'contatos':contatos
    })


def ver_contato(request, contato_id):
        contato = get_object_or_404(Contato,id=contato_id)

        if not contato.mostrar:
            raise Http404()
        return render(request,'usuarios/ver_contato.html',{
        'contato':contato
        })

def busca(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects.annotate(
        nome_completo =  campos
    ).filter(
        nome_completo__icontains=termo
    )
    paginator = Paginator(contatos, 20)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'usuarios/busca.html', {
        'contatos': contatos
    })

