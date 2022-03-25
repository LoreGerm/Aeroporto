from django.shortcuts import redirect, render
from App.models import Admin
from django.db.models import Q
from django.contrib import messages

# Create your views here.



def gestione_accesso(request):
    return render(request, 'App/pagina_gestione/log_in.html')


def verifica_accesso(request):
     if request.method == 'POST':
        nome = request.POST['nome']
        password = request.POST['password']
        if Admin.objects.filter(Q(nome=nome) & Q(password=password)):
            return render(request, 'App/pagina_gestione/home.html')
        else:
            messages.success(request, 'Accesso negato')
            return render(request, 'App/pagina_gestione/log_in.html')
            
