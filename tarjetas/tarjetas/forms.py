from django import forms
from .models import Tarjeta

class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ['tipo', 'puntaje']
        labels = {
            'tipo': 'Tipo de tarjeta',
            'puntaje': 'Puntaje'
        }
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'puntaje': forms.NumberInput(attrs={'class': 'form-control'})
        } 