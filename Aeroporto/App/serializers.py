from rest_framework import serializers
from .models import Volo, Aeroporto, Aereo, Indirizzo_a

class VoloJson(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Volo
        fields = ('id', 'codice', 'aeroporto_di_partenza', 'aeroporto_di_arrivo', 'prezzo_unitario', 'ora_di_partenza', 'ora_di_arrivo', 'data_di_partenza', 'data_di_arrivo', 'km', 'aereo')

    
class AeroportoJson(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aeroporto
        fields = ('codice', 'nome', 'indirizzo', 'descrizione')


class AereoJson(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aereo
        fields = ('targa', 'modello', 'stato', 'km_totali', 'km_da_ultima_manutenzione', 'data_ultima_manutenzione', 'posti_prima_classe', 'posti_seconda_classe', 'posti_terza_classe')


class Indirizzo_A_Json(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Indirizzo_a
        fields = ('via', 'numero', 'citta', 'provincia', 'stato')
