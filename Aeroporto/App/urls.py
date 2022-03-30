
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    #path('gestione', views.gestione_accesso, name='gestione'),
    #path('gestione/home', views.verifica_accesso, name='gestione_home'),
    path('gestione/home', views.gestione_home, name='gestione_home'),
    path('gestione/home/voli', views.gestione_voli, name='gestione_voli'),
    path('gestione/home/prenotazioni', views.gestione_prenotazioni, name='gestione_prenotazioni'),
    path('gestione/home/aeroporti', views.gestione_aeroporti, name='gestione_aeroporti'),

    path('gestione/home/voli/<int:id>', views.elimina_volo, name='elimina_volo'),
    path('gestione/home/voli/<int:id>', views.elimina_aeroporto, name='elimina_aeroporto'),
    path('gestione/home/voli/<int:id>', views.elimina_prenotazione, name='elimina_prenotazione'),
    
    path('gestione/home/voli/aggiungi', views.agg_voli, name='aggiungi_voli'),
    path('gestione/home/prenotazioni/aggiungi', views.agg_prenotazioni, name='aggiungi_prenotazioni'),
    path('gestione/home/aeroporti/aggiungi', views.agg_aeroporti, name='aggiungi_aeroporti'),
]