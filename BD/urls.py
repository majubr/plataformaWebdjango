from django.urls import path
from . import views

#usuarios
urlpatterns = [
    path('', views.index, name='BD'),
    path('<int:especie_id>', views.ver_especie, name='ver_especie'),
    path('busca/',views.busca, name='busca'),
    path('upload/',  views.data_upload, name='data_upload'),

]