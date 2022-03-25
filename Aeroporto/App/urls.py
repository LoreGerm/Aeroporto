
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('gestione', views.gestione_accesso, name='gestione'),
    path('gestione/home', views.verifica_accesso, name='gestione_home'),
    path('gestione/home/voli', views.gestione_voli, name='gestione_voli'),
]