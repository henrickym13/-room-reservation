from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib import messages


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
