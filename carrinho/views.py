from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ItemCarrinho
from gallery.models import Artwork

@login_required
def ver_carrinho(request):
    itens = ItemCarrinho.objects.filter(usuario=request.user).select_related('obra')
    total = sum((item.obra.price or 0) for item in itens)
    return render(request, 'carrinho/carrinho.html', {'itens': itens, 'total': total})

@login_required
def adicionar(request, obra_id):
    obra = get_object_or_404(Artwork, id=obra_id)
    ItemCarrinho.objects.get_or_create(usuario=request.user, obra=obra)
    return redirect('carrinho:ver_carrinho')

@login_required
def remover(request, obra_id):
    obra = get_object_or_404(Artwork, id=obra_id)
    ItemCarrinho.objects.filter(usuario=request.user, obra=obra).delete()
    return redirect('carrinho:ver_carrinho')
