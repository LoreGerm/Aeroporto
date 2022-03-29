from django.shortcuts import redirect, render
from App.models import Volo, Prenotazioni, Aeroporto
from App.models import Admin
from django.db.models import Q
from django.contrib import messages

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
        'obj':'voli',
        'voli':voli,
    }
    return render(request, 'App/pagina_gestione/gestione.html', content)


def gestione_prenotazioni(request):
    pren = Prenotazioni.objects.all()
    content = {
        'obj':'pren',
        'pren':pren,
    }
    return render(request, 'App/pagina_gestione/gestione.html', content)


def gestione_aeroporti(request):
    aeroporti = Aeroporto.objects.all()
    content = {
        'obj':'Aeroporti',
        'pren':aeroporti,
    }
    return render(request, 'App/pagina_gestione/gestione.html', content)


def elimina_volo(request, id):
    volo = Volo.objects.get(id = id)
    volo.delete()
    voli = Volo.objects.all()
    content = {
        'obj':'voli',
        'voli':voli,
    }
    return render(request, 'App/pagina_gestione/gestione.html', content)


def elimina_aeroporto(request, id):
    aeroporto = Aeroporto.objects.get(id = id)
    aeroporto.delete()
    aeroporti = Aeroporto.objects.all()
    content = {
        'obj':'Aeroporti',
        'pren':aeroporti,
    }
    return render(request, 'App/pagina_gestione/gestione.html', content)


def elimina_prenotazione(request, id):
    pren = Prenotazioni.objects.get(id = id)
    pren.delete()
    pren = Prenotazioni.objects.all()
    content = {
        'obj':'pren',
        'pren':pren,
    }
    return render(request, 'App/pagina_gestione/gestione.html', content)