from django import forms
from .models import Aereo, Indirizzo_a, Utente, Volo, Aeroporto, Prenotazioni

class VoloForm(forms.ModelForm):
    class Meta:
        model = Volo
        fields = ('codice', 'aeroporto_di_partenza', 'aeroporto_di_arrivo', 'prezzo_unitario', 'ora_di_partenza', 'ora_di_arrivo', 'data_di_partenza', 'data_di_arrivo', 'km', 'aereo')

        widgets =  {
            'codice': forms.TextInput(attrs={'class':'form-control'}),
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
        fields = ('utente', 'volo', 'posti_prenotati')

        widgets =  {
            'utente': forms.Select(attrs={'class':'form-select'}),
            'volo': forms.Select(attrs={'class':'form-select'}),
            'posti_prenotati': forms.TextInput(attrs={'class':'form-control'}),
        }


class AerportoForm(forms.ModelForm):
    class Meta:
        model = Aeroporto
        fields = ('codice', 'nome', 'indirizzo', 'descrizione')

        widgets =  {
            'codice': forms.TextInput(attrs={'class':'form-control'}),
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'descrizione': forms.Textarea(attrs={'class':'form-control'}),
        }


class Indirizzo_a_form(forms.ModelForm):
    class Meta:
        model = Indirizzo_a
        fields = '__all__'


class aereo_form(forms.ModelForm):
    class Meta:
        model = Aereo
        fields = '__all__'


class utente_form(forms.ModelForm):
    class Meta:
        model = Utente
        fields = '__all__'