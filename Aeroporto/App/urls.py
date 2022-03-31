
from . import views
from django.urls import path

urlpatterns = [
    #path('gestione', views.gestione_accesso, name='gestione'),
    #path('gestione/home', views.verifica_accesso, name='gestione_home'),
    path('gestione/home', views.gestione_home, name='gestione_home'),
    path('gestione/home/voli', views.gestione_voli, name='gestione_voli'),
    path('gestione/home/prenotazioni', views.gestione_prenotazioni, name='gestione_prenotazioni'),
    path('gestione/home/aeroporti', views.gestione_aeroporti, name='gestione_aeroporti'),

    path('gestione/home/voli/<int:id>', views.elimina_volo, name='elimina_volo'),
    path('gestione/home/aeroporti/<int:id>', views.elimina_aeroporto, name='elimina_aeroporto'),
    path('gestione/home/prenotazioni/<int:id>', views.elimina_prenotazione, name='elimina_prenotazione'),
    
    path('gestione/home/voli/aggiungi', views.agg_voli, name='aggiungi_voli'),
    path('gestione/home/voli/aggiungi/aereo', views.agg_aereo, name="aggiungi_aereo"),
    path('gestione/home/prenotazioni/aggiungi', views.agg_prenotazioni, name='aggiungi_prenotazioni'),
    path('gestione/home/prenotazioni/aggiungi/utente', views.agg_utente, name="aggiungi_utente"),
    path('gestione/home/aeroporti/aggiungi', views.agg_aeroporti, name='aggiungi_aeroporti'),
    path('gestione/home/aeroporti/aggiungi/indirizzo', views.agg_indirizzo_a, name="aggiungi_indirizzo_a"),

    path('gestione/home/voli/modifica/<int:id>', views.modifica_volo, name='modifica_volo'),
    path('gestione/home/aeroporti/modifica/<int:id>', views.modifica_aeroporto, name='modifica_aeroporto'),
    path('gestione/home/prenotazioni/modifica/<int:id>', views.modifica_prenotazione, name='modifica_prenotazione'),
]