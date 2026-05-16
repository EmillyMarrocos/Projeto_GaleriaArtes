from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import FormCadastro, FormPerfil
from .models import Perfil

def cadastro(request):
    if request.method == 'POST':
        form = FormCadastro(request.POST)
        if form.is_valid():
            usuario = form.save()
            tipo = form.cleaned_data['tipo']
            Perfil.objects.create(usuario=usuario, tipo=tipo)
            login(request, usuario)
            return redirect('accounts:perfil')
    else:
        form = FormCadastro()

    return render(request, 'accounts/cadastro.html', {'form': form})


def login_view(request):
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def perfil(request):
    perfil, _ = Perfil.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        form = FormPerfil(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('accounts:perfil')
    else:
        form = FormPerfil(instance=perfil)

    return render(request, 'accounts/perfil.html', {'form': form, 'perfil': perfil})
