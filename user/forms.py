from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label="Perfil de Usuário")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'group']
