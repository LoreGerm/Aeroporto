from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Admin(models.Model):
    nome = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    
    def __str__(self) -> str:
        return self.nome+' '+self.password



class Aereo(models.Model):
    codice = models.CharField(max_length=50, null=True, unique=True)
    modello = models.CharField(max_length=50, null=True, unique=True)
    in_volo = 'In volo'
    pronto = 'Pronto'
    man = 'Manutenzione'
    STATO = [(in_volo, 'In volo'),(pronto, 'Pronto'),(man, 'Manutenzione')]
    stato = models.CharField(max_length=50, null=True, choices=STATO)  
    km_totali = models.IntegerField(null=True)
    km_da_ultima_manutenzione = models.IntegerField(null=True)
    data_ultima_manutenzione = models.DateField(null=True)
    posti_prima_classe = models.IntegerField()
    posti_seconda_classe = models.IntegerField()
    posti_terza_classe = models.IntegerField()

    def __str__(self) -> str:
        return self.codice + ' ' + self.modello



class Indirizzo_a(models.Model):
    via = models.CharField(max_length=100, null=True)
    numero = models.CharField(max_length=100, null=True)
    citta = models.CharField(max_length=100, null=True)
    provincia = models.CharField(max_length=2, null=True)
    stato = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.via +' '+ self.numero+' '+self.citta + ' '+ self.provincia+' '+self.stato



class Aeroporto(models.Model):
    codice = models.CharField(max_length=200, null=True, unique=True)
    nome = models.CharField(max_length=100, null=True)
    indirizzo = models.ForeignKey(Indirizzo_a, on_delete=models.CASCADE)
    descrizione = models.CharField(max_length=500, null=True)

    def __str__(self) -> str:
        return self.nome



class Volo(models.Model):
    codice = models.CharField(max_length=200, null=True, unique=True)
    aeroporto_di_partenza = models.ForeignKey(Aeroporto, on_delete=models.CASCADE, related_name='aeroporto_partenza')
    aeroporto_di_arrivo = models.ForeignKey(Aeroporto, on_delete=models.CASCADE, related_name='aeroporto_arrivo', default=None)
    prezzo_unitario_prima_classe = models.FloatField(null=True, default=0.0)
    prezzo_unitario_seconda_classe = models.FloatField(null=True, default=0.0)
    prezzo_unitario_terza_classe = models.FloatField(null=True, default=0.0)    
    ora_di_partenza = models.TimeField(auto_now=False, auto_now_add=False)
    ora_di_arrivo = models.TimeField(auto_now=False, auto_now_add=False)
    data_di_partenza = models.DateField(null=True)
    data_di_arrivo = models.DateField(null=True)
    km = models.FloatField(null=True)
    aereo = models.ForeignKey(Aereo, on_delete=models.CASCADE)
    posti_totali = models.IntegerField()

    def __str__(self) -> str:
            return self.codice



class Utente(models.Model):
    nome = models.CharField(max_length=50, null=True)
    cognome = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    telefono = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.nome+' '+self.cognome


class Prenotazioni(models.Model):
    codice = models.CharField(max_length=200, null=False, unique=True)
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    volo = models.ForeignKey(Volo, on_delete=models.CASCADE)
    posti_prenotati = models.CharField(max_length=1000, null=True)
    prezzo_totale = models.FloatField(null=True)







