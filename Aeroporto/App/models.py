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
    in_volo = 'In volo'
    pronto = 'Pronto'
    man = 'Manutenzione'
    STATO = [(in_volo, 'In volo'),(pronto, 'Pronto'),(man, 'Manutenzione')]
    stato = models.CharField(max_length=50, null=True, choices=STATO)  
    km_totali = models.IntegerField(null=True)
    km_da_ultima_manutenzione = models.IntegerField(null=True)
    data_ultima_manutenzione = models.DateField(null=True)

    def __str__(self) -> str:
        return self.targa +' '+ self.modello


class Posti(models.Model):
    posti_prima_classe = models.IntegerField(null=True)
    posti_seconda_classe = models.IntegerField(null=True)
    posti_terza_classe = models.IntegerField(null=True)
    aereo = models.ForeignKey(Aereo, on_delete=models.CASCADE)



class Personale(models.Model):
    codice = models.CharField(max_length=200, null=True, unique=True)
    nome = models.CharField(max_length=50, null=True)
    cognome = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    telefono = models.CharField(max_length=100, null=True)
    stipendio = models.FloatField(null=True, default=0.0)
    in_volo = 'In volo'
    disp = 'Disponibile'
    ferie = 'Ferie'
    malattia = 'Malattia'
    STATO = [(in_volo, 'In volo'),(disp, 'Disponibile'),(ferie, 'Ferie'),(malattia, 'Malattia')]
    stato = models.CharField(max_length=50, null=True, choices=STATO)
    pilota = 'pilota'
    co_pi = 'Co-pilota'
    hostess = 'Hostess'
    RUOLO = [(pilota, 'Pilota'),(co_pi, 'Co-pilota'),(hostess, 'Hostess')]
    ruolo = models.CharField(max_length=50, null=True, choices=RUOLO)
    aereo = models.ForeignKey(Aereo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.codice +' '+ self.nome+' '+self.cognome


class Indirizzo_p(models.Model):
    via = models.CharField(max_length=100, null=True)
    numero = models.CharField(max_length=100, null=True)
    citta = models.CharField(max_length=100, null=True)
    provincia = models.CharField(max_length=2, null=True)
    stato = models.CharField(max_length=100, null=True)
    personale = models.ForeignKey(Personale, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.via +' '+ self.numero+' '+self.citta + ' '+ self.provincia+' '+self.stato



class Has_turni(models.Model):
    personale = models.ForeignKey(Personale, on_delete=models.CASCADE)
    turni = models.ForeignKey(Turni, on_delete=models.CASCADE)


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
    prezzo_unitario = models.FloatField(null=True, default=0.0)
    ora_di_partenza = models.TimeField(auto_now=False, auto_now_add=False)
    ora_di_arrivo = models.TimeField(auto_now=False, auto_now_add=False)
    data_di_partenza = models.DateField(null=True)
    data_di_arrivo = models.DateField(null=True)
    km = models.FloatField(null=True)
    aereo = models.ForeignKey(Aereo, on_delete=models.CASCADE)
    """
    posti_disponibili_prima_classe = models.IntegerField(default=aereo.posti_prima_classe)
    posti_disponibili_seconda_classe = models.IntegerField(default=aereo.posti_seconda_classe)
    posti_disponibili_terza_classe = models.IntegerField(default=aereo.posti_terza_classe)
"""
    def __str__(self) -> str:
            return self.codice


'''    
class Has_volo(models.Model):
    aeroporto = models.ForeignKey(Aeroporto, on_delete=models.CASCADE)
    volo = models.ForeignKey(Volo, on_delete=models.CASCADE)
'''



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
    posti_prenotati = ArrayField(models.CharField(max_length=10, null=True))







    



    



