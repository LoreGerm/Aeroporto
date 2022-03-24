from django.shortcuts import render

# Create your views here.



def gestione(request):
    return render(request, 'App/pagina_gestione/log_in.html')
