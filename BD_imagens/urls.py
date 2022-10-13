from django.urls import path
from . import views

#BD
urlpatterns = [
    path('', views.home, name='BD_imagens'),
    path('category/<slug:slug>', views.categoryPage, name='image-category'),
    path('category/<slug:slug1>/<slug:slug2>', views.imageDetailPage, name='image-detail'),
]



