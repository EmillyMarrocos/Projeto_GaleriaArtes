from django.urls import path
from . import views

app_name = "gallery"

urlpatterns = [
    path("", views.home, name="home"),
    path("obras/", views.artwork_list, name="artwork_list"),
    path("obras/nova/", views.artwork_create, name="artwork_create"),
    path("obras/<slug:slug>/", views.artwork_detail, name="artwork_detail"),
    path("obras/<slug:slug>/editar/", views.artwork_edit, name="artwork_edit"),
    path("artistas/", views.artist_list, name="artist_list"),
    path("artistas/<int:pk>/", views.artist_detail, name="artist_detail"),
]