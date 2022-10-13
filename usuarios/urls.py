from django.urls import path
from . import views

#usuarios
urlpatterns = [
    path('', views.index, name='usuarios'),
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
    path('busca/',views.busca, name='busca')
]