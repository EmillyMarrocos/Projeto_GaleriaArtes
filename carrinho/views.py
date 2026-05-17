from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ItemCarrinho
from gallery.models import Obra

@login_required
def ver_carrinho(request):
    itens = ItemCarrinho.objects.filter(usuario=request.user)
    total = sum(item.obra.preco for item in itens)
    return render(request, 'carrinho/carrinho.html')

@login_required
def adicionar(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)
    ItemCarrinho.objects.get_or_create(usuario=request.user, obra=obra)
    return redirect('ver_carrinho')

@login_required
def remover(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)
    ItemCarrinho.objects.filter(usuario=request.user, obra=obra).delete()
    return redirect('ver_carrinho')