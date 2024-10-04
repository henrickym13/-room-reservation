from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import Reserve
from .forms import ReserveForm, SeachAvailabilityForm
from room.models import Room


def is_admin(user):
    return user.is_superuser


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
@user_passes_test(is_admin)
def reserve_list(request):
    reservations_pending = Reserve.objects.filter(status='pendente')
    reservations_confirmed = Reserve.objects.filter(status='confirmada')
    return render(request, 'reserve_list.html', {
        'reservations_pending': reservations_pending,
        'reservations_confirmed': reservations_confirmed})


@login_required
def my_reserves(request):
    reserves = Reserve.objects.filter(user=request.user).exclude(status='cancelada')
    return render(request, 'my_reserves.html', {'reserves': reserves})


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


@login_required
@user_passes_test(is_admin)
def confirm_reservation(request, reserve_id):
    reserve = get_object_or_404(Reserve, id=reserve_id)
    if request.method == 'POST':
        reserve.status = 'confirmada'
        reserve.save()
        return redirect('reserve_list')
    
    return render(request, 'confirm_reserve.html', {'reserve': reserve})


@login_required
def cancel_reservation(request, reserve_id):
    reserve = get_object_or_404(Reserve, id=reserve_id, user=request.user)
    if request.method == 'POST':
        reserve.status = 'cancelada'
        reserve.save()
        return redirect('my_reserves')
    
    return render(request, 'cancel_reserve.html', {'reserve': reserve})