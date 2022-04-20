from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'volo', views.VoloApi)
router.register(r'aereo', views.AereoApi)
router.register(r'aeroporto', views.AeroportoApi)
router.register(r'indirizzo_a', views.Indirizzo_A_Api)
router.register(r'utente', views.UtenteApi)
router.register(r'prenotazione', views.PrenotazioneApi)

urlpatterns = [
    path('api', include(router.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),


    path('',views.prenota_utente, name='prenota_utente'),
    path('posti',views.scelta_posti, name='scelta_posti'),
    path('posti/utente',views.dati_utente, name='dati_utente'),
    path('posti/utente/recap',views.recap, name='recap'),
    path('posti/utente/recap/acquista',views.acquista, name='acquista'),

    path('i_tuoi_voli',views.i_tuoi_voli, name='i_tuoi_voli'),
    path('i_tuoi_voli/<int:id>',views.cancella_prenotazione, name='cancella_prenotazione'),

    #path('gestione', views.gestione_accesso, name='gestione'),
    #path('gestione/home', views.verifica_accesso, name='gestione_home'),
    path('gestione/home', views.gestione_home, name='gestione_home'),
    path('gestione/home/voli', views.gestione_voli, name='gestione_voli'),
    path('gestione/home/prenotazioni', views.gestione_prenotazioni, name='gestione_prenotazioni'),
    path('gestione/home/aeroporti', views.gestione_aeroporti, name='gestione_aeroporti'),
    path('gestione/home/aereo', views.gestione_aerei, name='gestione_aerei'),

    path('gestione/home/voli/<int:id>', views.elimina_volo, name='elimina_volo'),
    path('gestione/home/aeroporti/<int:id>', views.elimina_aeroporto, name='elimina_aeroporto'),
    path('gestione/home/prenotazioni/<int:id>', views.elimina_prenotazione, name='elimina_prenotazione'),
    path('gestione/home/aereo/<int:id>', views.elimina_aereo, name='elimina_aereo'),
    
    path('gestione/home/voli/aggiungi', views.agg_voli, name='aggiungi_voli'),
    path('gestione/home/voli/aereo', views.agg_aereo, name="aggiungi_aereo"),
    path('gestione/home/prenotazioni/aggiungi', views.agg_prenotazioni, name='aggiungi_prenotazioni'),
    path('gestione/home/aeroporti/aggiungi', views.agg_aeroporti, name='aggiungi_aeroporti'),

    path('gestione/home/voli/modifica/<int:id>', views.modifica_volo, name='modifica_volo'),
    path('gestione/home/aeroporti/modifica/<int:id>', views.modifica_aeroporto, name='modifica_aeroporto'),
    path('gestione/home/aerei/modifica/<int:id>', views.modifica_aereo, name='modifica_aereo'),

]