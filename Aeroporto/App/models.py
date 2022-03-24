from tkinter import CASCADE
from django.db import models

# Create your models here.


    


class Turni(models.Model):
    data = models.DateField(null=False)
    ora = models.DateField(null=False)


class Aereo(models.Model):
    targa = models.CharField(max_length=50, null=False, unique=True)
    modello = models.CharField(max_length=50, null=False, unique=True)
    stato = models.CharField(max_length=50, null=False, validators=['In_volo', 'Pronto', 'Manutenzione'])
    prima_classe = models.IntegerField(null=False)
    seconda_classe = models.IntegerField(null=False)
    terza_classe = models.IntegerField(null=False)
    km_totali = models.IntegerField(null=False)
    km_da_ultima_manutenzione = models.IntegerField(null=False)
    data_ultima_manutenzione = models.DateField(null=False)

    def __str__(self) -> str:
        return self.targa +' '+ self.modello+' '+self.stato+ ' '+ self.volo+' '+self.personale+' '+self.prima_classe+ ' '+ self.seconda_classe+' '+self.terza_classe+' '+self.km_totali+ ' '+ self.km_da_ultima_manutenzione+' '+self.data_ultima_manutenzione


class Personale(models.Model):
    codice = models.CharField(max_length=50, null=False, unique=True)
    nome = models.CharField(max_length=50, null=False)
    cognome = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100, null=False)
    stato = models.CharField(max_length=50, null=False, validators=['In_volo', 'Disponibile', 'Ferie', 'Malattia'])
    ruolo = models.CharField(max_length=50, null=False, validators=['Pilota', 'Co-pilota', 'Hostess'])
    aereo = models.ForeignKey(Aereo, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.codice +' '+ self.nome+' '+self.cognome+ ' '+ self.email+' '+self.stato+' '+self.ruolo+ ' '+ self.aereo



class Has_turni(models.Model):
    personale = models.ForeignKey(Personale, on_delete=models.SET_NULL)
    turni = models.ForeignKey(Turni, on_delete=models.SET_NULL)



class Indirizzo(models.Model):
    via = models.CharField(max_length=100, null=False)
    numero = models.CharField(max_length=100, null=False)
    citta = models.CharField(max_length=100, null=False)
    provincia = models.CharField(max_length=2, null=False)
    stato = models.CharField(max_length=100, null=False)
    personale = models.ForeignKey(Personale, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.via +' '+ self.numero+' '+self.citta + ' '+ self.provincia+' '+self.stato


class Aeroporto(models.Model):
    codice = models.CharField(max_length=200, null=False, unique=True)
    nome = models.CharField(max_length=100, null=False)
    descrizione = models.CharField(max_length=500, null=False)
    indirizzo = models.ForeignKey(Indirizzo, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.nome


class Volo(models.Model):
    codice = models.CharField(max_length=200, null=False, unique=True)
    aeroporto_p = models.ForeignKey(Aeroporto, on_delete=models.SET_NULL)
    aeroporto_a = models.ForeignKey(Aeroporto, on_delete=models.SET_NULL)
    ora_p = models.TimeField(auto_now=False, auto_now_add=False)
    ora_a = models.TimeField(auto_now=False, auto_now_add=False)
    data_p = models.DateField(null=False)
    data_a = models.DateField(null=False)
    km = models.FloatField(null=False)
    aereo = models.ForeignKey(Aereo, on_delete=models.SET_NULL)

    def __str__(self) -> str:
            return self.codice +' '+ self.aeroporto_p+' '+self.aeroporto_a+ ' '+ self.ora_p+' '+self.ora_a+' '+self.data_p+ ' '+ self.data_a+' '+self.km
    

class Has_volo(models.Model):
    aeroporto = models.ForeignKey(Aeroporto, on_delete=models.SET_NULL)
    volo = models.ForeignKey(Volo, on_delete=models.SET_NULL)






    



    



