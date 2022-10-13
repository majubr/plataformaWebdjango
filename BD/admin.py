from django.contrib import admin
from .models import Especie,ID_sp,ID_familia
# Register your models here.

class  EspecieAdmin(admin.ModelAdmin):
    list_display = ('id','Data','Ano','Estacao','Classe','Ordem','Familia',
                    'Genero','Especie','Nome_popular','Numero_registros','Metodologia','Ponto_amostral',
                    'Regiao','Latitude','Longitude','Altitude','Responsavel_tecnico','Projeto','Especialidade')
    list_display_links = ('id','Especie')
    list_filter = ('Especie','Responsavel_tecnico','Projeto','Especialidade')
    search_fields = ('Especie',)
    list_per_page = 10

class ID_spAdmin(admin.ModelAdmin):
    list_display = ('Especie',)
    list_display_links = ('Especie',)
    list_filter = ('Especie',)
    search_fields = ('Especie',)
    list_per_page = 10

class ID_familiaAdmin(admin.ModelAdmin):
    list_display = ('Familia',)
    list_display_links = ('Familia',)
    list_filter = ('Familia',)
    search_fields = ('Familia',)
    list_per_page = 10


admin.site.register(Especie, EspecieAdmin)

admin.site.register(ID_sp, ID_spAdmin)

admin.site.register(ID_familia, ID_familiaAdmin)


