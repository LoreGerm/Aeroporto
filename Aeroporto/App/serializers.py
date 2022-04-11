from rest_framework import serializers
from .models import Utente, Volo, Aeroporto, Aereo, Indirizzo_a, Prenotazioni





class Indirizzo_A_Json(serializers.ModelSerializer):
    class Meta:
        model = Indirizzo_a
        fields = ('via', 'numero', 'citta', 'provincia', 'stato')

class AeroportoJson(serializers.ModelSerializer):
    class Meta:
        model = Aeroporto
        fields = ('id', 'codice', 'nome', 'indirizzo', 'descrizione')


class AereoJson(serializers.ModelSerializer):
    class Meta:
        model = Aereo
        fields = ('targa', 'modello', 'stato', 'km_totali', 'km_da_ultima_manutenzione', 'data_ultima_manutenzione', 'posti_prima_classe', 'posti_seconda_classe', 'posti_terza_classe')


class VoloJson(serializers.ModelSerializer):
    aeroporto_di_partenza = AeroportoJson()
    aeroporto_di_arrivo = AeroportoJson()
    aereo = AereoJson()
    class Meta:
        model = Volo
        fields = ('codice', 'aeroporto_di_partenza', 'aeroporto_di_arrivo', 'prezzo_unitario_prima_classe', 'prezzo_unitario_seconda_classe', 'prezzo_unitario_terza_classe', 'ora_di_partenza', 'ora_di_arrivo', 'data_di_partenza', 'data_di_arrivo', 'km', 'aereo', 'posti_totali')

    

class Utente_Json(serializers.ModelSerializer):
    class Meta:
        model = Utente
        fields = ('nome', 'cognome', 'email', 'telefono') 



class Prenotazioni_Json(serializers.ModelSerializer):
    class Meta:
        model = Prenotazioni
        fields = ('codice', 'utente', 'volo', 'posti_prenotati', 'prezzo_totale')


