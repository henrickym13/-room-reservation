from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reserve
from .forms import ReserveForm, SeachAvailabilityForm
from room.models import Room


@login_required
def reserve_create(request):
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            reserve = form.save(commit=False)
            reserve.user = request.user
            reserve.save()
            return redirect('reserve_list')
    else:
        form = ReserveForm()
    return render(request, 'reserve_create.html', {'form': form})


@login_required
def reserve_list(request):
    reserves = Reserve.objects.filter(user=request.user)
    return render(request, 'reserve_list.html', {'reserves': reserves})


@login_required
def seach_availability(request):
    room_availability = None
    if request.method == 'POST':
        form = SeachAvailabilityForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['data']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']

            conflicting_reserves = Reserve.objects.filter(
                date=date,
                start_time__lt=start_time,
                end_time__gt=end_time
            ).values_list('room_id', flat=True)

            room_availability = Room.objects.exclude(id__in=conflicting_reserves)
    else:
        form = SeachAvailabilityForm()
        
    return render(request, 'seach_availability.html', {
        'form': form,
        'rooms_availability': room_availability})