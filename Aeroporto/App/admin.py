from django.contrib import admin
from django.contrib.auth.models import Group
from App.models import Aereo, Aeroporto, Personale, Posti, Turni, Volo, Admin, Utente, Prenotazioni, Indirizzo_p, Indirizzo_a

# Register your models here.
admin.site.unregister(Group)
admin.site.site_header = 'Starvato Airlines'
admin.site.site_title = 'Amministrazione'
admin.site.index_title = ''




class VoloAdmin(admin.ModelAdmin):
    list_display = ('codice', 'aeroporto_di_partenza', 'aeroporto_di_arrivo', 'prezzo_unitario_prima_classe', 'prezzo_unitario_seconda_classe', 'prezzo_unitario_terza_classe', 'ora_di_partenza', 'ora_di_arrivo', 'data_di_partenza', 'data_di_arrivo', 'km', 'aereo', 'posti_prima_classe', 'posti_seconda_classe', 'posti_terza_classe')
    list_filter = ('codice', 'aeroporto_di_partenza', 'aeroporto_di_arrivo', 'prezzo_unitario_prima_classe', 'prezzo_unitario_seconda_classe', 'prezzo_unitario_terza_classe', 'ora_di_partenza', 'ora_di_arrivo', 'data_di_partenza', 'data_di_arrivo', 'km', 'aereo', 'posti_prima_classe', 'posti_seconda_classe', 'posti_terza_classe')
admin.site.register(Volo, VoloAdmin)


class AeroportoAdmin(admin.ModelAdmin):
    list_display = ('codice', 'nome', 'indirizzo', 'descrizione')
    list_filter = ('codice', 'nome', 'indirizzo', 'descrizione')
admin.site.register(Aeroporto, AeroportoAdmin)

class PersonaleAdmin(admin.ModelAdmin):
    list_display = ('codice', 'nome', 'cognome', 'email', 'telefono', 'stipendio', 'stato', 'ruolo', 'aereo')
    list_filter = ('codice', 'nome', 'cognome', 'email', 'telefono', 'stipendio', 'stato', 'ruolo', 'aereo')
admin.site.register(Personale, PersonaleAdmin)

class AereoAdmin(admin.ModelAdmin):
    list_display = ('targa', 'modello', 'stato', 'km_totali', 'km_da_ultima_manutenzione', 'data_ultima_manutenzione')
    list_filter = ('targa', 'modello', 'stato', 'km_totali', 'km_da_ultima_manutenzione', 'data_ultima_manutenzione')
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
    list_display = ('codice', 'utente', 'volo', 'posti_prenotati', 'prezzo_totale')
    list_filter = ('codice', 'utente', 'volo', 'posti_prenotati', 'prezzo_totale')
admin.site.register(Prenotazioni, PrenotazioniAdmin)

class Indirizzo_p_Admin(admin.ModelAdmin):
    list_display = ('via', 'numero', 'citta', 'provincia', 'stato', 'personale')
    list_filter = ('via', 'numero', 'citta', 'provincia', 'stato', 'personale')
admin.site.register(Indirizzo_p, Indirizzo_p_Admin)

class Indirizzo_a_Admin(admin.ModelAdmin):
    list_display = ('via', 'numero', 'citta', 'provincia', 'stato')
    list_filter = ('via', 'numero', 'citta', 'provincia', 'stato')
admin.site.register(Indirizzo_a, Indirizzo_a_Admin)

class Posti_admin(admin.ModelAdmin):
    list_display = ('posti_prima_classe', 'posti_seconda_classe', 'posti_terza_classe', 'aereo')
    list_filter = ('posti_prima_classe', 'posti_seconda_classe', 'posti_terza_classe', 'aereo')
admin.site.register(Posti, Posti_admin)