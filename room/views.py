from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from .models import Room
from .forms import RoomForm
from reserve.models import Reserve


# Create your views here.
def is_admin(user):
    return user.groups.filter(name='Administradores').exists()


@login_required
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})


@login_required
def room_availability(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'room_availability.html', {'room': room})


@login_required
def event_room_availability(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    reserves = Reserve.objects.filter(room=room)
        
    eventos = []
    for reserve in reserves:
        eventos.append({
            'title': f"Reservado: {reserve.user.username}",
            'start': f"{reserve.date}T{reserve.start_time}",
            'end': f"{reserve.date}T{reserve.end_time}",
            'color': 'red',
        })
    return JsonResponse(eventos, safe=False)
    

@login_required
@user_passes_test(is_admin)
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'room_create.html', {'form': form})


@login_required
def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'room_detail.html', {'room': room})


@login_required
@user_passes_test(is_admin)
def update_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'room_update.html', {'form': form})
    

@login_required
@user_passes_test(is_admin)
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'room_delete.html', {'room' : room})