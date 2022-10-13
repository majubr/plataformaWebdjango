from django.urls import path
from . import views

#BD
urlpatterns = [
    path('', views.index, name='sobre')
]