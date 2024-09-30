from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reserve
from .forms import ReserveForm


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