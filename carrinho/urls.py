from django.urls import path
from . import views 

app_name = 'carrinho'

urlpatterns = [
    path('', views.ver_carrinho, name='ver_carrinho'),
    path('adicionar/<int:obra_id>/', views.adicionar, name='adicionar'),
    path('remover/<int:obra_id>/', views.remover, name='remover'),
]
