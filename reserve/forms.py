from django import forms
from .models import Reserve


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['room', 'date', 'start_time', 'end_time']
        widgets = {
            'room': forms.Select(choices=Reserve.objects.all(), attrs={'class': 'form-control'}),
            'date': forms.SelectDateWidget(attrs={'style': 'width: 27%; display: inline; margin-left: 12px;'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'room': 'Sala',
            'date': 'Data',
            'start_time': 'Hórario Inicial',
            'end_time': 'Hórario Final',
        }


class SeachAvailabilityForm(forms.Form):
    data = forms.DateTimeField(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label = 'Data'
    )
    start_time = forms.TimeField(
        widget = forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        label = 'Horário Inícial'
    )
    end_time = forms.TimeField(
        widget = forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        label = 'Horário Final'
    )