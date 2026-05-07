from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField()

    def __str__(self):
        return self.nome

class Obra(models.Model):
    CATEGORIAS = [
        ('PINTURA', 'Pintura'),
        ('CERAMICA', 'Cerâmica'),
        ('DESENHO', 'Desenho'),
        ('FOTOGRAFIA', 'Fotografia'), # Adicionada novas categorias de artes
    ]
    titulo = models.CharField(max_length=200)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagem = models.ImageField(upload_to='obras/')

    def __str__(self):
        return self.titulo