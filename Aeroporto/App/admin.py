from django.contrib import admin
from django.contrib.auth.models import Group
from App.models import Aereo, Aeroporto, Volo, Admin, Utente, Prenotazioni, Indirizzo_a

# Register your models here.
admin.site.unregister(Group)
admin.site.site_header = 'Starvato Airlines'
admin.site.site_title = 'Amministrazione'
admin.site.index_title = ''




class VoloAdmin(admin.ModelAdmin):
    list_display = ('codice', 'aeroporto_di_partenza', 'aeroporto_di_arrivo', 'prezzo_unitario_prima_classe', 'prezzo_unitario_seconda_classe', 'prezzo_unitario_terza_classe', 'ora_di_partenza', 'ora_di_arrivo', 'data_di_partenza', 'data_di_arrivo', 'km', 'aereo', 'posti_totali')
    list_filter = ('codice', 'aeroporto_di_partenza', 'aeroporto_di_arrivo', 'prezzo_unitario_prima_classe', 'prezzo_unitario_seconda_classe', 'prezzo_unitario_terza_classe', 'ora_di_partenza', 'ora_di_arrivo', 'data_di_partenza', 'data_di_arrivo', 'km', 'aereo', 'posti_totali')
admin.site.register(Volo, VoloAdmin)


class AeroportoAdmin(admin.ModelAdmin):
    list_display = ('codice', 'nome', 'indirizzo', 'descrizione')
    list_filter = ('codice', 'nome', 'indirizzo', 'descrizione')
admin.site.register(Aeroporto, AeroportoAdmin)


class AereoAdmin(admin.ModelAdmin):
    list_display = ('codice', 'modello', 'stato', 'km_totali', 'km_da_ultima_manutenzione', 'data_ultima_manutenzione')
    list_filter = ('codice', 'modello', 'stato', 'km_totali', 'km_da_ultima_manutenzione', 'data_ultima_manutenzione')
admin.site.register(Aereo, AereoAdmin)

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

class Indirizzo_a_Admin(admin.ModelAdmin):
    list_display = ('via', 'numero', 'citta', 'provincia', 'stato')
    list_filter = ('via', 'numero', 'citta', 'provincia', 'stato')
admin.site.register(Indirizzo_a, Indirizzo_a_Admin)









