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

    return redirect('gestione_voli')


def elimina_aeroporto(request, id):
    aeroporto = Aeroporto.objects.get(id = id)
    aeroporto.delete()
    
    return redirect('gestione_aeroporti')


def elimina_prenotazione(request, id):
    pren = Prenotazioni.objects.get(id = id)
    pren.delete()
    
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
    voli = []
    if request.method == 'POST':
        cerca = request.POST['cerca']
        voli = Volo.objects.filter(codice__icontains=cerca)
        
    content = {
        'agg': 'aggiungi_voli',
        'obj': voli,
        'voli': voli,
    }
    return render(request, 'App/pagina_gestione/cerca.html', content)


def cerca_prenotazioni(request):
    pass


def cerca_aeroporti(request):
    pass
