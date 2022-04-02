from django import forms
from .models import Aereo, Indirizzo_a, Utente, Volo, Aeroporto, Prenotazioni

class VoloForm(forms.ModelForm):
    class Meta:
        model = Volo
        fields = ('codice', 'aeroporto_di_partenza', 'aeroporto_di_arrivo', 'prezzo_unitario', 'ora_di_partenza', 'ora_di_arrivo', 'data_di_partenza', 'data_di_arrivo', 'km', 'aereo')

        widgets =  {
            'codice': forms.TextInput(attrs={'class':'form-control', 'id':'codice'}),
            'aeroporto_di_partenza': forms.Select(attrs={'class':'form-select'}),
            'aeroporto_di_arrivo': forms.Select(attrs={'class':'form-select'}),
            'prezzo_unitario': forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
            'ora_di_partenza': forms.TextInput(attrs={'class':'form-control', 'type':'time'}),
            'ora_di_arrivo': forms.TextInput(attrs={'class':'form-control', 'type':'time'}),
            'data_di_partenza': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            'data_di_arrivo': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            'km': forms.TextInput(attrs={'class':'form-control'}),
            'aereo': forms.Select(attrs={'class':'form-select'}),   #CREARE IL FORM PER GLI AEREI
        }


class PrenotaForm(forms.ModelForm):
    class Meta:
        model = Prenotazioni
        fields = ('codice', 'utente', 'volo', 'posti_prenotati')

        widgets =  {
            'codice': forms.TextInput(attrs={'class':'form-control', 'id':'codice'}),
            'utente': forms.Select(attrs={'class':'form-select'}),
            'volo': forms.Select(attrs={'class':'form-select', 'id':'volo'}),
            'posti_prenotati': forms.TextInput(attrs={'class':'d-non', 'id':'posti_prenotati'}),
        }


class AerportoForm(forms.ModelForm):
    class Meta:
        model = Aeroporto
        fields = ('codice', 'nome', 'indirizzo', 'descrizione')

        widgets =  {
            'codice': forms.TextInput(attrs={'class':'form-control'}),
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
            'numero': forms.TextInput(attrs={'class':'form-control'}),
            'citta': forms.TextInput(attrs={'class':'form-control'}),
            'provincia': forms.TextInput(attrs={'class':'form-control'}),
            'stato': forms.TextInput(attrs={'class':'form-control'}),
        }



class aereo_form(forms.ModelForm):
    class Meta:
        model = Aereo
        fields = ('targa', 'modello', 'stato', 'km_totali', 'km_da_ultima_manutenzione', 'data_ultima_manutenzione', 'posti_prima_classe', 'posti_seconda_classe', 'posti_terza_classe')

        widgets =  {
            'targa': forms.TextInput(attrs={'class':'form-control', 'name':'targa'}),
            'modello': forms.TextInput(attrs={'class':'form-control'}),
            'stato': forms.Select(attrs={'class':'form-select'}),
            'km_totali': forms.NumberInput(attrs={'class':'form-control', 'type':'number'}),
            'km_da_ultima_manutenzione': forms.NumberInput(attrs={'class':'form-control'}),
            'data_ultima_manutenzione': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'posti_prima_classe': forms.NumberInput(attrs={'class':'form-control', 'type':'number', 'name':'prima_classe'}),
            'posti_seconda_classe': forms.NumberInput(attrs={'class':'form-control', 'type':'number', 'name':'seconda_classe'}),
            'posti_terza_classe': forms.NumberInput(attrs={'class':'form-control', 'type':'number', 'name':'terza_classe'}),
        }



class utente_form(forms.ModelForm):
    class Meta:
        model = Utente
        fields = ('nome', 'cognome', 'email', 'telefono')

        widgets =  {
            'cognome': forms.TextInput(attrs={'class':'form-control'}),
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-select'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control'}),
        }



class personale_form(forms.ModelForm):
    pass