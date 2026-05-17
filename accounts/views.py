# pyrefly: ignore [missing-import]

from django.shortcuts import render, redirect
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
            return redirect('perfil')
        else:
            form = FormCadastro()
        return render(request, 'templates/cadastro.html', {'form': form})