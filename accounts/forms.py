from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class FormCadastro(UserCreationForm):
    email = forms.EmailField(required=True)
    tipo = forms.ChoiceField(
        choices=[
            ('comprador', 'Sou Comprador'), 
            ('artista', 'Sou Artista')
        ],
        widget = forms.RadioSelect
    )

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2', 'tipo']
    
class FormPerfil(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto', 'bio']