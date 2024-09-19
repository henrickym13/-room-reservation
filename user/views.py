from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data.get('group')
            group.user_set.add(user)
            messages.success(request, f'Conta criada para {user.username} no perfil de {group.name}!')
            login(request, user)
            return redirect('login')  # Redireciona após o cadastro
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Administradores').exists())
def admin_view(request):
    # Somente usuários do grupo "Administradores" podem acessar essa view
    return render(request, 'teste01.html')


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Funcionários').exists())
def funcionario_view(request):
    # Somente usuários do grupo "Funcionários" podem acessar essa view
    return render(request, 'teste02.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
