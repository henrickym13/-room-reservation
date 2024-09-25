from django import forms
from .models import Reserve


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['room', 'date', 'start_time', 'end_time']
        widgets = {
            'room': forms.Select(choices=Reserve.objects.all(), attrs={'class': 'form-control'}),
            'date': forms.SelectDateWidget(attrs={'style': 'width: 27%; display: inline; margin-left: 12px;'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'room': 'Sala',
            'date': 'Data',
            'start_time': 'Hórario Inicial',
            'end_time': 'Hórario Final',
        }