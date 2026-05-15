from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    TIPO_USUARIO = [
        ('comprador', 'Comprador'),
        ('artista', 'Artista'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO, default='comprador')
    foto = models.ImageField(upload_to='perfis/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def is_artista(self):
        return self.tipo == 'artista'

    def __str__(self):
        return f'{self.usuario.username}({self.tipo})'