from django.shortcuts import redirect, render
from App.models import Volo, Prenotazioni, Aeroporto, Indirizzo_a, Aereo, Utente
from App.models import Admin
from django.db.models import Q
from .forms import AerportoForm, Indirizzo_a_form, PrenotaForm, VoloForm, aereo_form, utente_form
from django.views.generic import CreateView

# Create your views here.


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
        'obj':'voli',
        'voli':voli,
    }
    return render(request, 'App/pagina_gestione/gestione.html', content)


def gestione_prenotazioni(request):
    pren = Prenotazioni.objects.all()
    content = {
        'agg': 'aggiungi_prenotazioni',
        'active_v': '',
        'active_p': 'active',
        'active_a': '',
        'obj': 'pren',
        'pren': pren,
    }
    return render(request, 'App/pagina_gestione/gestione.html', content)


def gestione_aeroporti(request):
    aeroporti = Aeroporto.objects.all()
    content = {
        'agg': 'aggiungi_aeroporti',
        'active_v': '',
        'active_p': '',
        'active_a': 'active',
        'obj': 'Aeroporti',
        'aeroporti': aeroporti,
    }
    return render(request, 'App/pagina_gestione/gestione.html', content)







def elimina_volo(request, id):
    volo = Volo.objects.get(id = id)
    volo.delete()
    voli = Volo.objects.all()

    return redirect('gestione_voli')


def elimina_aeroporto(request, id):
    aeroporto = Aeroporto.objects.get(id = id)
    aeroporto.delete()
    aeroporti = Aeroporto.objects.all()
    
    return redirect('gestione_aeroporti')


def elimina_prenotazione(request, id):
    pren = Prenotazioni.objects.get(id = id)
    pren.delete()
    pren = Prenotazioni.objects.all()
    
    return redirect('gestione_prenotazioni')







def agg_voli(request):
    messages = ''
    aeroporto = Aeroporto.objects.all()
    aereo = Aereo.objects.all()
    if request.method == 'POST':
        form = VoloForm(request.POST)
        if form.is_valid():
            form.save()
            messages = 'Salvato'
        else:
            messages = 'Errore'

    content = {
        'aeroporto': aeroporto,
        'aereo': aereo,
        'action': 'aggiungi_voli',
        'messaggio': messages,
        'home': 'gestione_voli',
    }
    return render(request, 'App/pagina_gestione/form/form_voli.html', content)

def agg_prenotazioni(request):
    messages = ''
    utente = Utente.objects.all()
    volo = Volo.objects.all()
    if request.method == 'POST':
        form = PrenotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages = 'Salvato'
        else:
            messages = 'Errore'

    content = {
        'volo': volo,
        'utente': utente,
        'action': 'aggiungi_prenotazioni',
        'messaggio': messages,
        'home': 'gestione_prenotazioni',
    }
    return render(request, 'App/pagina_gestione/form/form_prenota.html', content)

def agg_aeroporti(request):
    messages = ''
    indirizzi = Indirizzo_a.objects.all()
    if request.method == 'POST':
        form = AerportoForm(request.POST)
        if form.is_valid():
            form.save()
            messages = 'Salvato'
        else:
            messages = 'Errore'

    content = {
        'action': 'aggiungi_aeroporti',
        'messaggio': messages,
        'indirizzi': indirizzi,
        'home': 'gestione_aeroporti',
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
        'action': 'aggiungi_indirizzo_a',
        'messaggio': messages,
        'home': 'gestione_aeroporti',
    }
    return render(request, 'App/pagina_gestione/form/form_indirizzo_a.html', content) 

def agg_aereo(request):
    messages = ''
    if request.method == 'POST':
        form = aereo_form(request.POST)
        if form.is_valid():
            form.save()
            messages = 'Salvato'
        else:
            messages = 'Errore'

    content = {
        'action': 'aggiungi_aereo',
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
        'action': 'aggiungi_utente',
        'messaggio': messages,
        'home': 'gestione_prenotazioni',
    }
    return render(request, 'App/pagina_gestione/form/form_utente.html', content) 
