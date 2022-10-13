from typing import Tuple

from django.contrib import admin
from .models import Categoria, Contato
# Register your models here.

class  ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','telefone','email','formação',
                    'função','categoria','mostrar')
    list_display_links = ('id','nome','sobrenome')
    list_filter = ('nome','sobrenome','função')
    search_fields = ('nome','sobrenome','função')
    list_per_page = 10
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)

