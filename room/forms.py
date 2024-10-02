from django import forms
from .models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity', 'location', 'description', 'equipments']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control','rows': 3}),
            'equipments': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'name': 'Nome',
            'capacity': 'Capacidade',
            'location': 'Localização',
            'description': 'Descrição',
            'equipments': 'Equipamentos',
        }