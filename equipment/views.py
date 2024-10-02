from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Equipment

# Create your views here.
def is_admin(user):
    return user.groups.filter(name='Administradores').exists()


@login_required
def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment_list.html', {'equipments': equipments})


@login_required
@user_passes_test(is_admin)
def equipment_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Equipment.objects.create(name=name)
            return redirect('equipment_list')
    return render(request, 'equipment_create.html')