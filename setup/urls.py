from django.contrib import admin
from django.urls import path
from artistas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),         
    path('galeria/', views.galeria, name='galeria'), 
]