from django.urls import path
from . import views

#Home
urlpatterns = [
    path('', views.index, name='home')
]