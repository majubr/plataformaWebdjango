from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="dashboard"),
    path('relatorio_total_herpeto',views.relatorio_total_herpeto,name="relatorio_total_herpeto"),
    path('relatorio_herpeto',views.relatorio_herpeto,name='relatorio_herpeto')
]