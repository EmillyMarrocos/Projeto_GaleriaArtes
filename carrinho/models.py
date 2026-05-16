from django.db import models
from django.contrib.auth.models import User

class ItemCarrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    obra = models.ForeignKey('gallery.Artwork', on_delete=models.CASCADE)
    adicionado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.obra.title}'
