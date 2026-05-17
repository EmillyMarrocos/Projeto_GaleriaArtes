from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, verbose_name="Descrição")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name="Nome")
    bio = models.TextField(blank=True, verbose_name="Biografia")
    photo = models.ImageField(upload_to="artists/", blank=True, null=True, verbose_name="Foto")
    website = models.URLField(blank=True, verbose_name="Website")
    instagram = models.CharField(max_length=100, blank=True, verbose_name="Instagram")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artistas"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Artwork(models.Model):
    TECHNIQUE_CHOICES = [
        ("oil", "Óleo sobre tela"),
        ("acrylic", "Acrílico"),
        ("watercolor", "Aquarela"),
        ("digital", "Arte Digital"),
        ("sculpture", "Escultura"),
        ("photography", "Fotografia"),
        ("drawing", "Desenho"),
        ("other", "Outro"),
    ]

    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="artworks", verbose_name="Artista")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="artworks", verbose_name="Categoria")
    description = models.TextField(blank=True, verbose_name="Descrição")
    technique = models.CharField(max_length=20, choices=TECHNIQUE_CHOICES, default="other", verbose_name="Técnica")
    image = models.ImageField(upload_to="artworks/", verbose_name="Imagem")
    year = models.PositiveIntegerField(null=True, blank=True, verbose_name="Ano")
    dimensions = models.CharField(max_length=100, blank=True, verbose_name="Dimensões")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Preço")
    is_available = models.BooleanField(default=True, verbose_name="Disponível")
    is_featured = models.BooleanField(default=False, verbose_name="Destaque")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Obra"
        verbose_name_plural = "Obras"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} — {self.artist.name}"

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count(), 1)
        return None


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name="reviews", verbose_name="Obra")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name="Avaliação")
    comment = models.TextField(verbose_name="Comentário")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        ordering = ["-created_at"]
        unique_together = ["artwork", "user"]

    def __str__(self):        return f"{self.user.username} → {self.artwork.title} ({self.rating} estrelas)"