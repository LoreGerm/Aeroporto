
from django.shortcuts import redirect, render
from App.models import Volo, Prenotazioni, Aeroporto, Indirizzo_a, Aereo, Utente
from django.db.models import Q
from .forms import AerportoForm, Indirizzo_a_form, PrenotaForm, VoloForm, aereo_form, utente_form
from django.core.mail import send_mail

from rest_framework import viewsets
from .serializers import Prenotazioni_Json, Utente_Json, VoloJson, AereoJson, AeroportoJson, Indirizzo_A_Json


class VoloApi(viewsets.ModelViewSet):
    queryset = Volo.objects.all()
    serializer_class = VoloJson

class AereoApi(viewsets.ModelViewSet):
    queryset = Aereo.objects.all()
    serializer_class = AereoJson

class AeroportoApi(viewsets.ModelViewSet):
    queryset = Aeroporto.objects.all()
    serializer_class = AeroportoJson
    
class Indirizzo_A_Api(viewsets.ModelViewSet):
    queryset = Indirizzo_a.objects.all()
    serializer_class = Indirizzo_A_Json

class PrenotazioneApi(viewsets.ModelViewSet):
    queryset = Prenotazioni.objects.all()
    serializer_class = Prenotazioni_Json

class UtenteApi(viewsets.ModelViewSet):
    queryset = Utente.objects.all()
    serializer_class = Utente_Json





def prenota_utente(request):
    content = {
        'form_volo': VoloForm,
    }
    return render(request, 'App/pagine_utente/prenota/prenota.html', content)


# View chiamata una volta confermati i dati iniziali della prenotazione
def scelta_posti(request):
    posti = request.POST.get('posti', '')   # Numero di posti scelti
    codice_volo_andata = request.POST.get('andata', '') 
    codice_volo_ritorno = request.POST.get('ritorno', '')
    volo_ritorno = ''
    volo_andata = Volo.objects.get(codice = codice_volo_andata)
    # Se l'utente sceglie andata e ritorno
    if codice_volo_ritorno != '':   
        volo_ritorno = Volo.objects.get(codice = codice_volo_ritorno)

    content = {
        'form_prenota_andata': PrenotaForm,
        'form_prenota_ritorna': PrenotaForm,
        'volo_andata': volo_andata,
        'volo_ritorno': volo_ritorno,
        'posti': posti,
    }
    return render(request, 'App/pagine_utente/prenota/scelta_posti.html', content)

# View chiamata dopo aver scelto i posti
def dati_utente(request):
    if request.method == 'POST':
        id_volo_andata = request.POST.get('id_volo_andata', '')
        id_volo_ritorno = request.POST.get('id_volo_ritorno', '')
        volo_andata = Volo.objects.get(id = id_volo_andata)
        posti_prenotati_andata = request.POST.get('posti_prenotati_andata', '')
        prezzo_totale_andata = request.POST.get('prezzo_totale_andata', '')

        volo_ritorno = ''
        posti_prenotati_ritorno = ''
        prezzo_totale_ritorno = ''
        # Se l'utente sceglie andata e ritorno
        if id_volo_ritorno != '':
            volo_ritorno = Volo.objects.get(id = id_volo_ritorno)
            posti_prenotati_ritorno = request.POST.get('posti_prenotati_ritorno', '')
            prezzo_totale_ritorno = request.POST.get('prezzo_totale_ritorno', '')

    content = {
        'form_utente': utente_form,
        'volo_andata': volo_andata,
        'volo_ritorno': volo_ritorno,
        'posti_prenotati_andata': posti_prenotati_andata,
        'posti_prenotati_ritorno': posti_prenotati_ritorno,
        'prezzo_totale_andata': prezzo_totale_andata,
        'prezzo_totale_ritorno': prezzo_totale_ritorno,
    }
    return render(request, 'App/pagine_utente/prenota/form_utente.html', content)

# View chiamata dopo aver messo i dati dell'utente
def recap(request):
    if request.method == 'POST':
        nome_ut = request.POST['nome']
        cognome_ut = request.POST['cognome']
        email_ut = request.POST['email']
        telefono_ut = request.POST['telefono']
        id_volo_andata = request.POST.get('id_volo_andata', '')
        id_volo_ritorno = request.POST.get('id_volo_ritorno', '')

        volo_andata = Volo.objects.get(id = id_volo_andata)
        posti_prenotati_andata = request.POST.get('posti_prenotati_andata', '')
        prezzo_totale_andata = request.POST.get('prezzo_totale_andata', '')

        volo_ritorno = ''
        posti_prenotati_ritorno = ''
        prezzo_totale_ritorno = ''
        # Se l'utente sceglie andata e ritorno
        if id_volo_ritorno != '':
            volo_ritorno = Volo.objects.get(id = id_volo_ritorno)
            posti_prenotati_ritorno = request.POST.get('posti_prenotati_ritorno', '')
            prezzo_totale_ritorno = request.POST.get('prezzo_totale_ritorno', '')

    content = {
        'prenota_form_andata': PrenotaForm,
        'prenota_form_ritorno': PrenotaForm,
        'nome_ut': nome_ut,
        'cognome_ut': cognome_ut,
        'email_ut': email_ut,
        'telefono_ut': telefono_ut,
        'volo_andata': volo_andata,
        'volo_ritorno': volo_ritorno,
        'posti_prenotati_andata': posti_prenotati_andata,
        'posti_prenotati_ritorno': posti_prenotati_ritorno,
        'prezzo_totale_andata': prezzo_totale_andata,
        'prezzo_totale_ritorno': prezzo_totale_ritorno,
    }
    return render(request, 'App/pagine_utente/prenota/recap.html', content)

# View chiamata una volta confermata la prenotazione
def acquista(request):
    if request.method == 'POST':
        # Crea l'utente e lo salva
        nome = request.POST.get('nome', '')
        cognome = request.POST.get('cognome', '')
        email = request.POST.get('email', '')
        telefono = int(request.POST.get('telefono', ''))
        utente = Utente(nome=nome, cognome=cognome, email=email, telefono=telefono)
        utente.save()

        codice_pre = request.POST.get('codice', '')

        volo_ritorno_id = request.POST.get('volo_ritorno_id', '')
        volo_ritorno = ''
        # Se l'utente sceglie andata e ritorno
        if volo_ritorno_id != '':
            volo_ritorno = Volo.objects.get(id=volo_ritorno_id)
            posti_ritorno = request.POST.get('posti_prenotati_ritorno', '')
            # Modifica i posti totali del volo togliendo quelli scelti
            volo_ritorno.posti_totali -= len(list(posti_ritorno.split(',')))
            volo_ritorno.save() # Salva la modifica
            prezzo_totale_ritorno = request.POST.get('prezzo_totale_ritorno', '')
            prenotazione_ritorno = Prenotazioni(codice=codice_pre, utente=utente, volo=volo_ritorno, posti_prenotati=posti_ritorno, prezzo_totale=prezzo_totale_ritorno)
            prenotazione_ritorno.save()

        volo_andata_id = request.POST.get('volo_andata_id', '')
        volo_andata = Volo.objects.get(id=volo_andata_id)
        posti_andata = request.POST.get('posti_prenotati_andata', '')
        # Modifica i posti totali del volo togliendo quelli scelti
        volo_andata.posti_totali -= len(list(posti_andata.split(',')))
        volo_andata.save() # Salva la modifica

        # Crea la prenotazione
        prezzo_totale_andata = request.POST.get('prezzo_totale_andata', '')
        prenotazione_andata = Prenotazioni(codice=codice_pre, utente=utente, volo=volo_andata, posti_prenotati=posti_andata, prezzo_totale=prezzo_totale_andata)
        prenotazione_andata.save()

        # Manda la mail con il codice
        if volo_ritorno_id != '':
            send_mail(
                'Codice prenotazione Starlato Airline',
                'Codice della prenotazione:   Andata --> '+codice_pre[0] + ' Ritorno --> '+codice_pre[1],
                'loregerm149@gmail.com',
                [email],
                fail_silently=False,
            )
        else:
            send_mail(
                'Codice prenotazione Starlato Airline',
                'Codice della prenotazione:   Andata --> '+codice_pre[0],
                'loregerm149@gmail.com',
                [email],
                fail_silently=False,
            )

    content = {
        'codice': codice_pre,
        'volo_ritorno': volo_ritorno,
    }
    return render(request, 'App/pagine_utente/prenota/acquista.html', content)



# View chiamata quando si vogliono visualizzare le prenotazioni
def i_tuoi_voli(request):
    content = {
    }
    return render(request, 'App/pagine_utente/i_tuoi_voli.html', content)

# View chiamata quando l'utente vuole eliminare la prenotazione
def cancella_prenotazione(request,id):
    pren = Prenotazioni.objects.get(id = id)
    utente = Utente.objects.get(id = pren.utente.id)
    # Prenotazioni con lo stesso utente
    pren_con_ut = Prenotazioni.objects.filter(utente = utente.id)

    volo = Volo.objects.get(id = pren.volo.id)
    posti_pren = len(list(pren.posti_prenotati.split(',')))
    # i posti della prenotazione vengono riaggiunti al volo
    volo.posti_totali += posti_pren

    # Se lo stesso utente appare in una sola prenotazione viene eliminato
    if len(pren_con_ut) <= 1:
        utente.delete()
    pren.delete()
    volo.save()
    
    return redirect('i_tuoi_voli')










#######################################################################################



def gestione_home(request):
    return render(request, 'App/pagina_gestione/home.html')



def gestione_voli(request):
    content = {
        'agg': 'aggiungi_voli',
        'active_v': 'active',
        'active_p': '',
        'active_a': '',
        'active_ae': '',
        'obj':'voli',
        'cerca': 'cerca_voli',
    }
    return render(request, 'App/pagina_gestione/gestione.html', content)


def gestione_prenotazioni(request):
    content = {
        'active_v': '',
        'active_p': 'active',
        'active_a': '',
        'active_ae': '',
        'obj': 'pren',
        'cerca': 'cerca_prenotazioni',
    }
    return render(request, 'App/pagina_gestione/gestione.html', content)


def gestione_aeroporti(request):
    content = {
        'agg': 'aggiungi_aeroporti',
        'active_v': '',
        'active_p': '',
        'active_a': 'active',
        'active_ae': '',
        'obj': 'aeroporti',
        'cerca': 'cerca_aeroporti',
    }
    return render(request, 'App/pagina_gestione/gestione.html', content)


def gestione_aerei(request):
    content = {
        'agg': 'aggiungi_aereo',
        'active_v': '',
        'active_p': '',
        'active_a': '',
        'active_ae': 'active',
        'obj': 'aerei',
        'cerca': 'cerca_aereo',
    }
    return render(request, 'App/pagina_gestione/gestione.html', content)







def elimina_volo(request, id):
    volo = Volo.objects.get(id = id)
    volo.delete()

    return redirect('gestione_voli')


def elimina_aeroporto(request, id):
    aeroporto = Aeroporto.objects.get(id = id)
    aeroporto.delete()
    
    return redirect('gestione_aeroporti')


def elimina_prenotazione(request, id):
    pren = Prenotazioni.objects.get(id = id)
    utente = Utente.objects.get(id = pren.utente.id)
    pren_con_ut = Prenotazioni.objects.filter(utente = utente.id)
    print(pren_con_ut)
    volo = Volo.objects.get(id = pren.volo.id)
    posti_pren = len(list(pren.posti_prenotati.split(',')))
    volo.posti_totali += posti_pren
    if len(pren_con_ut) <= 1:
        utente.delete()
    pren.delete()
    volo.save()

    return redirect('gestione_prenotazioni')


def elimina_aereo(request, id):
    aereo = Aereo.objects.get(id = id)
    aereo.delete()
    
    return redirect('gestione_aerei')





def modifica_volo(request, id):
    volo = Volo.objects.get(id = id)
    field = {
        'codice': volo.codice,
        'aeroporto_di_partenza': volo.aeroporto_di_partenza,
        'aeroporto_di_arrivo': volo.aeroporto_di_arrivo,
        'prezzo_unitario_prima_classe': volo.prezzo_unitario_prima_classe,
        'prezzo_unitario_seconda_classe': volo.prezzo_unitario_seconda_classe,
        'prezzo_unitario_terza_classe': volo.prezzo_unitario_terza_classe,
        'ora_di_partenza': volo.ora_di_partenza,
        'ora_di_arrivo': volo.ora_di_arrivo,
        'data_di_partenza': volo.data_di_partenza,
        'data_di_arrivo': volo.data_di_arrivo,
        'km': volo.km,
        'aereo': volo.aereo,
        'posti_totali':volo.posti_totali,
    }
    form = VoloForm(initial=field)
    messages = ''
    aereo_in = Aereo.objects.get(id = volo.aereo.id)

    tot_posti_aereo = int(aereo_in.posti_prima_classe)+int(aereo_in.posti_seconda_classe)+int(aereo_in.posti_terza_classe)
    posti_occupati = tot_posti_aereo - int(volo.posti_totali)

    if request.method == 'POST':
        try:
            volo.codice = request.POST.get('codice', '')
            aeroporto_partenza = Aeroporto.objects.get(id = request.POST.get('aeroporto_di_partenza', ''))
            volo.aeroporto_di_partenza = aeroporto_partenza
            aeroporto_arrivo = Aeroporto.objects.get(id = request.POST.get('aeroporto_di_arrivo', ''))
            volo.aeroporto_di_arrivo = aeroporto_arrivo

            volo.prezzo_unitario_prima_classe = request.POST.get('prezzo_unitario_prima_classe', '')
            volo.prezzo_unitario_seconda_classe = request.POST.get('prezzo_unitario_seconda_classe', '')
            volo.prezzo_unitario_terza_classe = request.POST.get('prezzo_unitario_terza_classe', '')
            volo.ora_di_partenza = request.POST.get('ora_di_partenza', '')
            volo.ora_di_arrivo = request.POST.get('ora_di_arrivo', '')
            volo.data_di_partenza = request.POST.get('data_di_partenza', '')
            volo.data_di_arrivo = request.POST.get('data_di_arrivo', '')
            volo.km = request.POST.get('km', '')
            aereo_mod = Aereo.objects.get(id = request.POST.get('aereo', ''))
            volo.aereo = aereo_mod

            # Se si cambia l'aereo al volo ai nuovi posti totali vengono tolti i posti già prenotati
            if(aereo_in != aereo_mod):
                volo.posti_totali = int(request.POST.get('posti_totali', '')) - posti_occupati
            volo.save()
            messages = 'Salvato' 
        except:
           messages = 'Errore'
       

    content = {
        'form': form,
        'messaggio': messages,
        'home': 'gestione_voli',
    }
    return render(request, 'App/pagina_gestione/form/form_voli.html', content)


def modifica_aeroporto(request, id):
    aeroporto = Aeroporto.objects.get(id = id)
    indirizzo = Indirizzo_a.objects.get(id = aeroporto.indirizzo.id)
    messages = ''
    field_a={
        'codice': aeroporto.codice,
        'nome': aeroporto.nome,
        'indirizzo': aeroporto.indirizzo,
        'descrizione': aeroporto.descrizione,
    }
    form_i = Indirizzo_a_form()
    form_a = AerportoForm(initial=field_a)
    if request.method == 'POST':
        # Se l'utente non crea un nuovo indirizzo
        if request.POST.get('via', '') != '': 
            try:
                indirizzo.via = request.POST.get('via', '')
                indirizzo.numero = request.POST.get('numero', '')
                indirizzo.citta = request.POST.get('citta', '')
                indirizzo.provincia = request.POST.get('provincia', '')
                indirizzo.stato = request.POST.get('stato', '')
                indirizzo.save()

                aeroporto.codice = request.POST.get('codice', '')
                aeroporto.nome = request.POST.get('nome', '')
                aeroporto.indirizzo = indirizzo
                aeroporto.descrizione = request.POST.get('descrizione', '')
                aeroporto.save()
                messages = 'Salvato'
            except:
                messages = 'Errore'
        else:
            try:
                indirizzo = Indirizzo_a.objects.get(id = request.POST.get('indirizzo', ''))
                aeroporto.codice = request.POST.get('codice', '')
                aeroporto.nome = request.POST.get('nome', '')
                aeroporto.indirizzo = indirizzo
                aeroporto.descrizione = request.POST.get('descrizione', '')
                aeroporto.save()
                messages = 'Salvato'
            except:
                messages = 'Errore'                

    content = {
        'messaggio': messages,
        'home': 'gestione_aeroporti',
        'form_a': form_a,
        'form_i': form_i,
    }
    return render(request, 'App/pagina_gestione/form/form_aeroporto.html', content) 



def modifica_aereo(request, id):
    aereo = Aereo.objects.get(id = id)
    field = {
        'codice': aereo.codice,
        'modello': aereo.modello,
        'stato': aereo.stato,
        'km_totali': aereo.km_totali,
        'km_da_ultima_manutenzione': aereo.km_da_ultima_manutenzione,
        'data_ultima_manutenzione': aereo.data_ultima_manutenzione,
        'posti_prima_classe': aereo.posti_prima_classe,
        'posti_seconda_classe': aereo.posti_seconda_classe,
        'posti_terza_classe': aereo.posti_terza_classe,
    }
    form = aereo_form(initial=field)
    messages = ''
    if request.method == 'POST':
        form = aereo_form(request.POST, instance=aereo)
        if form.is_valid():
            form.save()
            messages = 'Salvato'
        else:
            messages = 'Errore'

    content = {
        'form': form,
        'messaggio': messages,
        'home': 'gestione_aerei',
    }
    return render(request, 'App/pagina_gestione/form/form_aereo.html', content)





#################################### AGGIUNGI ################################################




def agg_voli(request):
    messages = ''
    if request.method == 'POST':
        form = VoloForm(request.POST)
        if form.is_valid():
            form.save()
            messages = 'Salvato'
        else:
            messages = 'Errore'

    content = {
        'form': VoloForm,
        'messaggio': messages,
        'home': 'gestione_voli',
    }
    return render(request, 'App/pagina_gestione/form/form_voli.html', content)



def agg_aeroporti(request):
    messages = ''
    if request.method == 'POST':
        # Se l'utente non crea un nuovo indirizzo
        if request.POST.get('via', '') != '':
            try:
                indirizzo = Indirizzo_a(via=request.POST.get('via', ''), numero=request.POST.get('numero', ''), citta=request.POST.get('citta', ''), provincia=request.POST.get('provincia', ''), stato=request.POST.get('stato', ''))
                indirizzo.save()
                aeroporto = Aeroporto(codice=request.POST.get('codice', ''), nome=request.POST.get('nome', ''), indirizzo=indirizzo, descrizione=request.POST.get('descrizione', ''))
                aeroporto.save()
                messages = 'Salvato'
            except:
                messages = 'Errore'
        else:
            indirizzo = Indirizzo_a.objects.get(id = request.POST.get('indirizzo', ''))
            aeroporto = Aeroporto(codice=request.POST.get('codice', ''), nome=request.POST.get('nome', ''), indirizzo=indirizzo, descrizione=request.POST.get('descrizione', ''))
            aeroporto.save()

    content = {
        'messaggio': messages,
        'home': 'gestione_aeroporti',
        'form_a': AerportoForm,
        'form_i': Indirizzo_a_form,
    }
    return render(request, 'App/pagina_gestione/form/form_aeroporto.html', content) 



def agg_aereo(request):
    messages = ''
    if request.method == 'POST':
        form = aereo_form(request.POST)
        print()
        if form.is_valid():
            form.save()
            messages = 'Salvato'
        else:
            messages = 'Errore'
    

    content = {
        'form': aereo_form,
        'messaggio': messages,
        'home': 'gestione_aerei',
    }
    return render(request, 'App/pagina_gestione/form/form_aereo.html', content) 




