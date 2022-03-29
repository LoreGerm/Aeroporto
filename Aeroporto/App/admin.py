from django.contrib import admin
from django.contrib.auth.models import Group
from App.models import Aereo, Aeroporto, Personale, Turni, Volo, Admin, Utente, Prenotazioni, Indirizzo

# Register your models here.
admin.site.unregister(Group)
admin.site.site_header = 'Starvato Airlines'
admin.site.site_title = 'Amministrazione'
admin.site.index_title = ''




class VoloAdmin(admin.ModelAdmin):
    list_display = ('codice', 'aeroporto_partenza', 'aeroporto_arrivo', 'prezzo_unitario', 'ora_partenza', 'ora_arrivo', 'data_partenza', 'data_arrivo', 'posti_disponibili_prima_classe', 'posti_disponibili_seconda_classe', 'posti_disponibili_terza_classe', 'km', 'aereo')
    list_filter = ('codice', 'aeroporto_partenza', 'aeroporto_arrivo', 'prezzo_unitario', 'ora_partenza', 'ora_arrivo', 'data_partenza', 'data_arrivo', 'posti_disponibili_prima_classe', 'posti_disponibili_seconda_classe', 'posti_disponibili_terza_classe', 'km', 'aereo')
admin.site.register(Volo, VoloAdmin)


class AeroportoAdmin(admin.ModelAdmin):
    list_display = ('codice', 'nome', 'descrizione', 'indirizzo')
    list_filter = ('codice', 'nome', 'descrizione', 'indirizzo')
admin.site.register(Aeroporto, AeroportoAdmin)

class PersonaleAdmin(admin.ModelAdmin):
    list_display = ('codice', 'nome', 'cognome', 'email', 'telefono', 'stipendio', 'stato', 'ruolo', 'aereo')
    list_filter = ('codice', 'nome', 'cognome', 'email', 'telefono', 'stipendio', 'stato', 'ruolo', 'aereo')
admin.site.register(Personale, PersonaleAdmin)

class AereoAdmin(admin.ModelAdmin):
    list_display = ('targa', 'modello', 'stato', 'posti_prima_classe', 'posti_seconda_classe', 'posti_terza_classe', 'km_totali', 'km_da_ultima_manutenzione', 'data_ultima_manutenzione')
    list_filter = ('targa', 'modello', 'stato', 'posti_prima_classe', 'posti_seconda_classe', 'posti_terza_classe', 'km_totali', 'km_da_ultima_manutenzione', 'data_ultima_manutenzione')
admin.site.register(Aereo, AereoAdmin)

class TurniAdmin(admin.ModelAdmin):
    list_display = ('data', 'ora')
    list_filter = ('data', 'ora')
admin.site.register(Turni, TurniAdmin)

class AdminAdmin(admin.ModelAdmin):
    list_display = ('nome', 'password')
    list_filter = ('nome', 'password')
admin.site.register(Admin, AdminAdmin)

class UtenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cognome', 'email', 'telefono')
    list_filter = ('nome', 'cognome', 'email', 'telefono')
admin.site.register(Utente, UtenteAdmin)

class PrenotazioniAdmin(admin.ModelAdmin):
    list_display = ('utente', 'volo', 'posti_prenotati')
    list_filter = ('utente', 'volo', 'posti_prenotati')
admin.site.register(Prenotazioni, PrenotazioniAdmin)

class IndirizzoAdmin(admin.ModelAdmin):
    list_display = ('via', 'numero', 'citta', 'provincia', 'stato', 'personale')
    list_filter = ('via', 'numero', 'citta', 'provincia', 'stato', 'personale')
admin.site.register(Indirizzo, IndirizzoAdmin)