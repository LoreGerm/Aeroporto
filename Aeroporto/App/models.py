from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Admin(models.Model):
    nome = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    
    def __str__(self) -> str:
        return self.nome+' '+self.password



class Turni(models.Model):
    data = models.DateField(null=True)
    ora = models.DateField(null=True)
    
    def __str__(self) -> str:
        return self.data+' '+self.ora



class Aereo(models.Model):
    targa = models.CharField(max_length=50, null=True, unique=True)
    modello = models.CharField(max_length=50, null=True, unique=True)
    stato = models.CharField(max_length=50, null=True)    #['In_volo', 'Pronto', 'Manutenzione']
    posti_prima_classe = models.IntegerField(null=True)
    posti_seconda_classe = models.IntegerField(null=True)
    posti_terza_classe = models.IntegerField(null=True)
    km_totali = models.IntegerField(null=True)
    km_da_ultima_manutenzione = models.IntegerField(null=True)
    data_ultima_manutenzione = models.DateField(null=True)

    def __str__(self) -> str:
        return self.targa +' '+ self.modello+' '+self.stato+ ' '+ self.volo+' '+self.personale+' '+self.prima_classe+ ' '+ self.seconda_classe+' '+self.terza_classe+' '+self.km_totali+ ' '+ self.km_da_ultima_manutenzione+' '+self.data_ultima_manutenzione



class Personale(models.Model):
    codice = models.CharField(max_length=50, null=True, unique=True)
    nome = models.CharField(max_length=50, null=True)
    cognome = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    telefono = models.CharField(max_length=100, null=True, default=0)
    stipendio = models.FloatField(null=True, default=0.0)
    stato = models.CharField(max_length=50, null=True)   #['In_volo', 'Disponibile', 'Ferie', 'Malattia']
    ruolo = models.CharField(max_length=50, null=True)   #['Pilota', 'Co-pilota', 'Hostess']
    aereo = models.ForeignKey(Aereo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.codice +' '+ self.nome+' '+self.cognome+' '+self.stato+' '+self.ruolo+ ' '+ self.aereo



class Has_turni(models.Model):
    personale = models.ForeignKey(Personale, on_delete=models.CASCADE)
    turni = models.ForeignKey(Turni, on_delete=models.CASCADE)



class Indirizzo(models.Model):
    via = models.CharField(max_length=100, null=True)
    numero = models.CharField(max_length=100, null=True)
    citta = models.CharField(max_length=100, null=True)
    provincia = models.CharField(max_length=2, null=True)
    stato = models.CharField(max_length=100, null=True)
    personale = models.ForeignKey(Personale, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.via +' '+ self.numero+' '+self.citta + ' '+ self.provincia+' '+self.stato



class Aeroporto(models.Model):
    codice = models.CharField(max_length=200, null=True, unique=True)
    nome = models.CharField(max_length=100, null=True)
    descrizione = models.CharField(max_length=500, null=True)
    indirizzo = models.ForeignKey(Indirizzo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome



class Volo(models.Model):
    codice = models.CharField(max_length=200, null=True, unique=True)
    aeroporto = models.ForeignKey(Aeroporto, on_delete=models.CASCADE)
    #aeroporto_a = models.ForeignKey(Aeroporto, on_delete=models.CASCADE)
    prezzo_unitario = models.FloatField(null=True, default=0.0)
    ora_partenza = models.TimeField(auto_now=False, auto_now_add=False)
    ora_arrivo = models.TimeField(auto_now=False, auto_now_add=False)
    data_partenza = models.DateField(null=True)
    data_arrivo = models.DateField(null=True)
    km = models.FloatField(null=True)
    aereo = models.ForeignKey(Aereo, on_delete=models.CASCADE)

    def __str__(self) -> str:
            return self.codice +' '+ self.aeroporto+' '+self.prezzo_unitario+' '+ self.ora_partenza+' '+self.ora_arrivo+' '+self.data_partenza+ ' '+ self.data_arrivo+' '+self.km
    

class Has_volo(models.Model):
    aeroporto = models.ForeignKey(Aeroporto, on_delete=models.CASCADE)
    volo = models.ForeignKey(Volo, on_delete=models.CASCADE)



class Utente(models.Model):
    nome = models.CharField(max_length=50, null=True)
    cognome = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    telefono = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.nome+' '+self.cognome


class Prenotazioni(models.Model):
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    volo = models.ForeignKey(Volo, on_delete=models.CASCADE)
    posti_prenotati = ArrayField(models.CharField(max_length=10, null=True))







    



    



