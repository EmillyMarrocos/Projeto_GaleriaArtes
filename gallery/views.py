from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Artwork, Category, Artist, Review
from .forms import ArtworkForm, ReviewForm


def home(request):
    featured = Artwork.objects.filter(is_featured=True).select_related("artist")[:6]
    recent = Artwork.objects.order_by("-created_at").select_related("artist")[:8]
    categories = Category.objects.all()
    artists = Artist.objects.all()[:6]

    context = {
        "featured": featured,
        "recent": recent,
        "categories": categories,
        "artists": artists,
    }
    return render(request, "gallery/home.html", context)


def artwork_list(request):
    artworks = Artwork.objects.select_related("artist", "category").all()

    # Filtros
    category_slug = request.GET.get("category")
    technique = request.GET.get("technique")
    search = request.GET.get("q")
    available = request.GET.get("available")

    if category_slug:
        artworks = artworks.filter(category__slug=category_slug)

    if technique:
        artworks = artworks.filter(technique=technique)

    if search:
        artworks = artworks.filter(
            Q(title__icontains=search) |
            Q(artist__name__icontains=search) |
            Q(description__icontains=search)
        )

    if available == "1":
        artworks = artworks.filter(is_available=True)

    categories = Category.objects.all()
    technique_choices = Artwork.TECHNIQUE_CHOICES

    context = {
        "artworks": artworks,
        "categories": categories,
        "technique_choices": technique_choices,
        "selected_category": category_slug,
        "selected_technique": technique,
        "search_query": search,
    }
    return render(request, "gallery/artwork_list.html", context)


def artwork_detail(request, slug):
    artwork = get_object_or_404(Artwork.objects.select_related("artist", "category"), slug=slug)
    reviews = artwork.reviews.select_related("user").all()
    related = Artwork.objects.filter(category=artwork.category).exclude(pk=artwork.pk)[:4]

    user_review = None
    review_form = None

    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()
        if not user_review:
            review_form = ReviewForm()

    if request.method == "POST" and request.user.is_authenticated:
        if user_review:
            messages.warning(request, "Você já avaliou esta obra.")
        else:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.artwork = artwork
                review.user = request.user
                review.save()
                messages.success(request, "Avaliação enviada com sucesso!")
                return redirect("gallery:artwork_detail", slug=slug)

    context = {
        "artwork": artwork,
        "reviews": reviews,
        "related": related,
        "user_review": user_review,
        "review_form": review_form,
        "average_rating": artwork.average_rating(),
    }
    return render(request, "gallery/artwork_detail.html", context)


@login_required
def artwork_create(request):
    # Verifica se o usuário tem um perfil de artista
    try:
        artist = request.user.artist
    except Artist.DoesNotExist:
        messages.error(request, "Você precisa ter um perfil de artista para cadastrar obras.")
        return redirect("gallery:home")

    if request.method == "POST":
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.artist = artist
            artwork.save()
            messages.success(request, f'Obra "{artwork.title}" criada com sucesso!')
            return redirect("gallery:artwork_detail", slug=artwork.slug)
    else:
        form = ArtworkForm()

    return render(request, "gallery/artwork_form.html", {"form": form, "action": "Criar"})


@login_required
def artwork_edit(request, slug):
    artwork = get_object_or_404(Artwork, slug=slug)

    try:
        artist = request.user.artist
    except Artist.DoesNotExist:
        messages.error(request, "Acesso negado.")
        return redirect("gallery:home")

    if artwork.artist != artist:
        messages.error(request, "Você não tem permissão para editar esta obra.")
        return redirect("gallery:artwork_detail", slug=slug)

    if request.method == "POST":
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            messages.success(request, "Obra atualizada com sucesso!")
            return redirect("gallery:artwork_detail", slug=slug)
    else:
        form = ArtworkForm(instance=artwork)

    return render(request, "gallery/artwork_form.html", {"form": form, "action": "Editar", "artwork": artwork})


def artist_list(request):
    artists = Artist.objects.prefetch_related("artworks").all()
    context = {"artists": artists}
    return render(request, "gallery/artist_list.html", context)


def artist_detail(request, pk):
    artist = get_object_or_404(Artist.objects.prefetch_related("artworks__category"), pk=pk)
    artworks = artist.artworks.all()
    context = {"artist": artist, "artworks": artworks}
    return render(request, "gallery/artist_detail.html", context)
