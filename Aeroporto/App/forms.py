from django import forms
from .models import Aereo, Indirizzo_a, Utente, Volo, Aeroporto, Prenotazioni

class VoloForm(forms.ModelForm):
    class Meta:
        model = Volo
        fields = ('codice', 'aeroporto_di_partenza', 'aeroporto_di_arrivo', 'prezzo_unitario_prima_classe', 'prezzo_unitario_seconda_classe', 'prezzo_unitario_terza_classe', 'ora_di_partenza', 'ora_di_arrivo', 'data_di_partenza', 'data_di_arrivo', 'km', 'aereo', 'posti_totali')

        widgets =  {
            'codice': forms.TextInput(attrs={'class':'form-control', 'id':'codice', 'name':'codice'}),
            'aeroporto_di_partenza': forms.Select(attrs={'class':'form-select', 'name':'aeroporto_di_partenza', 'id':'aeroporto_di_partenza'}),
            'aeroporto_di_arrivo': forms.Select(attrs={'class':'form-select', 'name': 'aeroporto_di_arrivo', 'id':'aeroporto_di_arrivo'}),
            'prezzo_unitario_prima_classe': forms.TextInput(attrs={'class':'form-control', 'type':'number', 'step':'0.01', 'min':'0'}),
            'prezzo_unitario_seconda_classe': forms.TextInput(attrs={'class':'form-control', 'type':'number', 'step':'0.01', 'min':'0'}),
            'prezzo_unitario_terza_classe': forms.TextInput(attrs={'class':'form-control', 'type':'number', 'step':'0.01', 'min':'0'}),
            'ora_di_partenza': forms.TextInput(attrs={'class':'form-control', 'type':'time'}),
            'ora_di_arrivo': forms.TextInput(attrs={'class':'form-control', 'type':'time'}),
            'data_di_partenza': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            'data_di_arrivo': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            'km': forms.TextInput(attrs={'class':'form-control'}),
            'aereo': forms.Select(attrs={'class':'form-select', 'onchange':'Imposta_posti_volo()', 'id':'aereo'}),
            'posti_totali': forms.NumberInput(attrs={'id':'posti_totali', 'name':'posti_totali'}),
        }


class PrenotaForm(forms.ModelForm):
    class Meta:
        model = Prenotazioni
        fields = ('codice', 'utente', 'volo', 'posti_prenotati', 'prezzo_totale')

        widgets =  {
            'codice': forms.TextInput(attrs={'class':'form-control', 'id':'codice', 'name':'codice'}),
            'utente': forms.Select(attrs={'class':'form-select'}),
            'volo': forms.Select(attrs={'class':'form-select', 'id':'volo', 'name':'volo'}),
            'posti_prenotati': forms.TextInput(attrs={'id':'posti_prenotati', 'name':'posti_prenotati'}),
            'prezzo_totale': forms.NumberInput(attrs={'class':'form-control', 'value':0, 'step':'0.01', 'name':'prezzo_totale'}),
        }


class AerportoForm(forms.ModelForm):
    class Meta:
        model = Aeroporto
        fields = ('codice', 'nome', 'indirizzo', 'descrizione')

        widgets =  {
            'codice': forms.TextInput(attrs={'class':'form-control', 'id':'codice', 'name':'codice'}),
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'indirizzo': forms.Select(attrs={'class':'form-select'}),
            'descrizione': forms.Textarea(attrs={'class':'form-control'}),
        }


class Indirizzo_a_form(forms.ModelForm):
    class Meta:
        model = Indirizzo_a
        fields = ('via', 'numero', 'citta', 'provincia', 'stato')

        widgets =  {
            'via': forms.TextInput(attrs={'class':'form-control'}),
            'numero': forms.TextInput(attrs={'class':'form-control', 'min':'1'}),
            'citta': forms.TextInput(attrs={'class':'form-control'}),
            'provincia': forms.TextInput(attrs={'class':'form-control'}),
            'stato': forms.TextInput(attrs={'class':'form-control'}),
        }



class aereo_form(forms.ModelForm):
    class Meta:
        model = Aereo
        fields = ('codice', 'modello', 'stato', 'km_totali', 'km_da_ultima_manutenzione', 'data_ultima_manutenzione', 'posti_prima_classe', 'posti_seconda_classe', 'posti_terza_classe')

        widgets =  {
            'codice': forms.TextInput(attrs={'class':'form-control', 'name':'codice', 'id':'codice'}),
            'modello': forms.TextInput(attrs={'class':'form-control'}),
            'stato': forms.Select(attrs={'class':'form-select'}),
            'km_totali': forms.NumberInput(attrs={'class':'form-control', 'type':'number', 'min':'0'}),
            'km_da_ultima_manutenzione': forms.NumberInput(attrs={'class':'form-control', 'min':'0'}),
            'data_ultima_manutenzione': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'posti_prima_classe': forms.NumberInput(attrs={'class':'form-control', 'type':'number', 'name':'prima_classe', 'min':'1'}),
            'posti_seconda_classe': forms.NumberInput(attrs={'class':'form-control', 'type':'number', 'name':'seconda_classe', 'min':'1'}),
            'posti_terza_classe': forms.NumberInput(attrs={'class':'form-control', 'type':'number', 'name':'terza_classe', 'min':'1'}),
        }



class utente_form(forms.ModelForm):
    class Meta:
        model = Utente
        fields = ('nome', 'cognome', 'email', 'telefono')

        widgets =  {
            'cognome': forms.TextInput(attrs={'class':'form-control', 'name':'cognome'}),
            'nome': forms.TextInput(attrs={'class':'form-control', 'name':'nome'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'name':'email'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control', 'name':'telefono'}),
        }


