from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reserve.models import Reserve


@login_required
def index(request):
    reserves = Reserve.objects.filter(user=request.user).order_by('-date')
    return render(request, 'index.html', {'reserves': reserves})