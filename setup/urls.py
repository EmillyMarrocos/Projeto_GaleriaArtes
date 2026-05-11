from django.contrib import admin
from django.urls import path
from artistas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home_alias'),         
    path('galeria/', views.galeria, name='galeria'), 
    path('login/', views.login_view, name='login'),
    path('perfil/', views.perfil, name='perfil'),
]