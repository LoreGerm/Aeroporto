import json
from wsgiref.handlers import format_date_time
from django.shortcuts import redirect, render
from App.models import Volo, Prenotazioni, Aeroporto, Indirizzo_a, Aereo, Utente
from App.models import Admin
from django.db.models import Q
from .forms import AerportoForm, Indirizzo_a_form, PrenotaForm, VoloForm, aereo_form, utente_form
from django.views.generic import CreateView
from django.templatetags.static import static

# Create your views here.

def prenota_utente(request):
    voli = []
    if request.method == 'POST':
        partenza = request.POST['aeroporto_di_partenza']
        arrivo = request.POST['aeroporto_di_arrivo']
        data_partenza = request.POST['data_di_partenza']
        data_arrivo = request.POST['data_di_arrivo']
        voli = Volo.objects.filter(Q(aeroporto_di_partenza = partenza) & Q(aeroporto_di_arrivo = arrivo) & Q(data_di_partenza = data_partenza) & Q(data_di_arrivo = data_arrivo))

    content = {
        'form_volo': VoloForm,
        'voli': voli,
    }
    return render(request, 'App/pagine_utente/prenota.html', content)

def scelta_posti(request, id):
    volo = Volo.objects.get(id = id)
    content = {
        'form_prenota': PrenotaForm,
        'volo': volo,
    }
    return render(request, 'App/pagine_utente/scelta_posti.html', content)

def dati_utente(request):
    if request.method == 'POST':
        volo_id = request.POST.get('id_volo', '')
        volo = Volo.objects.get(id = volo_id)
        posti = request.POST['posti_prenotati']

    content = {
        'form_utente': utente_form,
        'volo': volo,
        'posti': posti,
        'prezzo_tot': int(volo.prezzo_unitario) * len(list(posti.split(","))),
    }
    return render(request, 'App/pagine_utente/form_utente.html', content)

def recap(request):
    if request.method == 'POST':
        nome_ut = request.POST['nome']
        cognome_ut = request.POST['cognome']
        email_ut = request.POST['email']
        telefono_ut = request.POST['telefono']
        volo_id = request.POST.get('id_volo', '')
        volo = Volo.objects.get(id = volo_id)
        posti = request.POST['posti']
        prezzo_tot = request.POST['prezzo_tot']

    content = {
        'prenota_form': PrenotaForm,
        'nome_ut': nome_ut,
        'cognome_ut': cognome_ut,
        'email_ut': email_ut,
        'telefono_ut': telefono_ut,
        'volo': volo,
        'posti': posti,
        'prezzo_tot': prezzo_tot,
    }
    return render(request, 'App/pagine_utente/recap.html', content)

def acquista(request):
    if request.method == 'POST':
        codice_pre = request.POST['codice']
        nome = request.POST.get('nome', '')
        cognome = request.POST.get('cognome', '')
        email = request.POST.get('email', '')
        telefono = int(request.POST.get('telefono', ''))
        #form_ut = utente_form(nome,cognome,email,telefono) ######### ERRORE + POSTI DINAMICI
        volo_id = request.POST.get('volo', '')
        posti = request.POST.get('posti', '')
        prezzo_tot = request.POST.get('prezzo_tot', '')

        print(nome)
        print(cognome)
        print(email)
        print(telefono)
        print(volo_id)
        print(posti)
        print(prezzo_tot)

    content = {
        'codice': codice_pre,
    }
    return render(request, 'App/pagine_utente/acquista.html', content)






















#######################################################################################

def gestione_accesso(request):
    return render(request, 'App/pagina_gestione/log_in.html')

def gestione_home(request):
    return render(request, 'App/pagina_gestione/home.html')
"""
def verifica_accesso(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        password = request.POST['password']
        if Admin.objects.filter(Q(nome=nome) & Q(password=password)):
            return render(request, 'App/pagina_gestione/home.html')
        else:
            messages.success(request, 'Accesso negato')
            return render(request, 'App/pagina_gestione/log_in.html')
            """


def gestione_voli(request):
    voli = Volo.objects.all()
    content = {
        'agg': 'aggiungi_voli',
        'active_v': 'active',
        'active_p': '',
        'active_a': '',
        'active_ae': '',
        'obj':'voli',
        'voli':voli,
        'cerca': 'cerca_voli',
    }
    return render(request, 'App/pagina_gestione/gestione.html', content)


def gestione_prenotazioni(request):
    pren = Prenotazioni.objects.all()
    content = {
        'agg': 'aggiungi_prenotazioni',
        'active_v': '',
        'active_p': 'active',
        'active_a': '',
        'active_ae': '',
        'obj': 'pren',
        'pren': pren,
        'cerca': 'cerca_prenotazioni',
    }
    return render(request, 'App/pagina_gestione/gestione.html', content)


def gestione_aeroporti(request):
    aeroporti = Aeroporto.objects.all()
    content = {
        'agg': 'aggiungi_aeroporti',
        'active_v': '',
        'active_p': '',
        'active_a': 'active',
        'active_ae': '',
        'obj': 'Aeroporti',
        'aeroporti': aeroporti,
        'cerca': 'cerca_aeroporti',
    }
    return render(request, 'App/pagina_gestione/gestione.html', content)


def gestione_aerei(request):
    aerei = Aereo.objects.all()
    content = {
        'agg': 'aggiungi_aereo',
        'active_v': '',
        'active_p': '',
        'active_a': '',
        'active_ae': 'active',
        'obj': 'aerei',
        'aerei': aerei,
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
    pren.delete()
    
    return redirect('gestione_prenotazioni')


def elimina_aereo(request, id):
    aereo = Aereo.objects.get(id = id)
    aereo.delete()
    
    return redirect('gestione_prenotazioni')





def modifica_volo(request, id):
    volo = Volo.objects.get(id = id)
    field = {
        'codice': volo.codice,
        'aeroporto_di_partenza': volo.aeroporto_di_partenza,
        'aeroporto_di_arrivo': volo.aeroporto_di_arrivo,
        'prezzo_unitario': volo.prezzo_unitario,
        'ora_di_partenza': volo.ora_di_partenza,
        'ora_di_arrivo': volo.ora_di_arrivo,
        'data_di_partenza': volo.data_di_partenza,
        'data_di_arrivo': volo.data_di_arrivo,
        'km': volo.km,
        'aereo': volo.aereo,
    }
    form = VoloForm(initial=field)
    messages = ''
    if request.method == 'POST':
        form = VoloForm(request.POST, instance=volo)
        if form.is_valid():
            form.save()
            messages = 'Salvato'
        else:
            messages = 'Errore'

    content = {
        'form': form,
        'messaggio': messages,
        'home': 'gestione_voli',
    }
    return render(request, 'App/pagina_gestione/form/form_voli.html', content)


def modifica_aeroporto(request, id):
    aeroporto = Aeroporto.objects.get(id = id)
    messages = ''
    field={
        'codice': aeroporto.codice,
        'nome': aeroporto.nome,
        'indirizzo': aeroporto.indirizzo,
        'descrizione': aeroporto.descrizione,
    }
    form = AerportoForm(initial=field)
    if request.method == 'POST':
        form = AerportoForm(request.POST)
        if form.is_valid():
            form.save()
            messages = 'Salvato'
        else:
            messages = 'Errore'

    content = {
        'messaggio': messages,
        'home': 'gestione_aeroporti',
        'form': form,
    }
    return render(request, 'App/pagina_gestione/form/form_aeroporto.html', content) 
    


def modifica_prenotazione(request, id):
    pren = Prenotazioni.objects.get(id = id)
    messages = ''
    field={
        'utente': pren.utente,
        'volo': pren.volo,
        'posti_prenotati': pren.posti_prenotati,
    }
    form = PrenotaForm(initial=field)
    if request.method == 'POST':
        form = PrenotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages = 'Salvato'
        else:
            messages = 'Errore'

    content = {
        'messaggio': messages,
        'home': 'gestione_prenotazioni',
        'form': form,
    }
    return render(request, 'App/pagina_gestione/form/form_prenota.html', content) 


def modifica_aereo(request, id):
    aereo = Aereo.objects.get(id = id)
    field = {
        'targa': aereo.targa,
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


def agg_prenotazioni(request):
    messages = ''
    if request.method == 'POST':
        form = PrenotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages = 'Salvato'
        else:
            messages = 'Errore'

    content = {
        'form': PrenotaForm,
        'messaggio': messages,
        'home': 'gestione_prenotazioni',
    }
    return render(request, 'App/pagina_gestione/form/form_prenota.html', content)


def agg_aeroporti(request):
    messages = ''
    if request.method == 'POST':
        form = AerportoForm(request.POST)
        if form.is_valid():
            form.save()
            messages = 'Salvato'
        else:
            messages = 'Errore'

    # INSERISCI NEL FILE JSON IL NUMERO DI POSTI E FALLO LEGGERE AL JS PER GENEREARE I POSTI
    # {'prima':numero-posti, 'seconda':numero-posti, 'terza':numero-posti,}

    content = {
        'messaggio': messages,
        'home': 'gestione_aeroporti',
        'form': AerportoForm,
    }
    return render(request, 'App/pagina_gestione/form/form_aeroporto.html', content) 


def agg_indirizzo_a(request):
    messages = ''
    if request.method == 'POST':
        form = Indirizzo_a_form(request.POST)
        if form.is_valid():
            form.save()
            messages = 'Salvato'
        else:
            messages = 'Errore'

    content = {
        'form': Indirizzo_a_form,
        'messaggio': messages,
        'home': 'gestione_aeroporti',
    }
    return render(request, 'App/pagina_gestione/form/form_indirizzo_a.html', content) 




def Stampa(file):
    f = open(file, "r")
    a = f.read()
    f.close()
    return a

def Over_write(file,x):
    f = open(file, "w")
    f.write(json.dumps(x)) 
    f.close()


def agg_aereo(request):
    messages = ''
    if request.method == 'POST':
        form = aereo_form(request.POST)
        if form.is_valid():
            all_posti = []
            all_posti.append(Stampa(static('js/posti.json')))
            posti = {
                'targa': request.POST['targa'],
                'prima': request.POST['prima_classe'],
                'seconda': request.POST['seconda_classe'],
                'terza': request.POST['terza_classe'],
            }
            all_posti.append(posti)
            Over_write('static/js/posti.json',all_posti)
            form.save()
            messages = 'Salvato'
        else:
            messages = 'Errore'

    content = {
        'form': aereo_form,
        'messaggio': messages,
        'home': 'gestione_voli',
    }
    return render(request, 'App/pagina_gestione/form/form_aereo.html', content) 


def agg_utente(request):
    messages = ''
    if request.method == 'POST':
        form = utente_form(request.POST)
        if form.is_valid():
            form.save()
            messages = 'Salvato'
        else:
            messages = 'Errore'

    content = {
        'form': utente_form,
        'messaggio': messages,
        'home': 'gestione_prenotazioni',
    }
    return render(request, 'App/pagina_gestione/form/form_utente.html', content) 




def cerca_voli(request):
    voli = ''
    if request.method == 'POST':
        cerca = request.POST.get('cerca', '')
        voli = Volo.objects.filter(codice__icontains=cerca)
        
    content = {
        'agg': 'aggiungi_voli',
        'active_v': 'active',
        'active_p': '',
        'active_a': '',
        'active_ae': '',
        'obj':'voli',
        'voli':voli,
        'cerca': 'cerca_voli',
    }
    return render(request, 'App/pagina_gestione/cerca.html', content)


def cerca_prenotazioni(request):
    pren = []
    if request.method == 'POST':
        cerca = request.POST.get('cerca', '')
        pren = Prenotazioni.objects.filter(Q(codice__icontains=cerca) | Q(utente__nome__icontains=cerca) | Q(utente__cognome__icontains=cerca))

    content = {
        'agg': 'aggiungi_prenotazioni',
        'active_v': '',
        'active_p': 'active',
        'active_a': '',
        'active_ae': '',
        'obj': 'pren',
        'pren': pren,
        'cerca': 'cerca_prenotazioni',
    }
    return render(request, 'App/pagina_gestione/cerca.html', content)


def cerca_aeroporti(request):
    aeroporto = []
    if request.method == 'POST':
        cerca = request.POST.get('cerca', '')
        aeroporto = Aeroporto.objects.filter(Q(codice__icontains=cerca) | Q(nome__icontains=cerca))

    content = {
        'agg': 'aggiungi_aeroporti',
        'active_v': '',
        'active_p': '',
        'active_a': 'active',
        'active_ae': '',
        'obj': 'Aeroporti',
        'aeroporti': aeroporto,
        'cerca': 'cerca_aeroporti',
    }
    return render(request, 'App/pagina_gestione/cerca.html', content)


def cerca_aereo(request):
    aereo = []
    if request.method == 'POST':
        cerca = request.POST.get('cerca', '')
        aereo = Aereo.objects.filter(Q(targa__icontains=cerca) | Q(modello__icontains=cerca))

    content = {
        'agg': 'aggiungi_aereo',
        'active_v': '',
        'active_p': '',
        'active_a': '',
        'active_ae': 'active',
        'obj': 'aerei',
        'aerei': aereo,
        'cerca': 'cerca_aereo',
    }
    return render(request, 'App/pagina_gestione/cerca.html', content)




def json_posti(request):

    f = open('static/js/posti.json', 'w')
    f.write(json.dumps())