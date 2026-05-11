from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def galeria(request):
    # Dados simulados (Mock Data)
    obras_falsas = [
        {
            'nome': 'Noite Estrelada',
            'artista': 'Vincent van Gogh',
            'categoria': 'Pintura',
            'imagem_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/960px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg'
        },
        {
            'nome': 'O Grito',
            'artista': 'Edvard Munch',
            'categoria': 'Expressionismo',
            'imagem_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Edvard_Munch%2C_1893%2C_The_Scream%2C_oil%2C_tempera_and_pastel_on_cardboard%2C_91_x_73_cm%2C_National_Gallery_of_Norway.jpg/500px-Edvard_Munch%2C_1893%2C_The_Scream%2C_oil%2C_tempera_and_pastel_on_cardboard%2C_91_x_73_cm%2C_National_Gallery_of_Norway.jpg'
        },
        {
            'nome': 'Moça com Brinco de Pérola',
            'artista': 'Johannes Vermeer',
            'categoria': 'Barroco',
            'imagem_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Johannes_Vermeer_%281632-1675%29_-_The_Girl_With_The_Pearl_Earring_%281665%29.jpg/500px-Johannes_Vermeer_%281632-1675%29_-_The_Girl_With_The_Pearl_Earring_%281665%29.jpg'
        },

        {
            'nome': 'O beijo Roubado',
            'artista': 'Jean Honoré Fragonard',
            'categoria': 'Barroco',
            'imagem_url': 'https://www.ocasaldafoto.com/wp-content/uploads/2024/10/rococo%CC%81.jpg'
        },
    ]

    # Lógica da Barra de Pesquisa
    busca = request.GET.get('buscar')
    if busca:
        # Filtra na lista se o termo estiver no nome ou no artista (ignora maiúsculas/minúsculas)
        obras_falsas = [o for o in obras_falsas if busca.lower() in o['nome'].lower() or busca.lower() in o['artista'].lower()]

    return render(request, 'galeria.html', {'obras': obras_falsas})

def login_view(request):
    return render(request, 'login.html')

def perfil(request):
    usuario_falso = {
        'nome': 'Emilly Marrocos',
        'email': 'emilly.marrocos@exemplo.com',
        'avatar': 'https://github.com/EmillyMarrocos.png'
    }

    contexto = {
        'usuario': usuario_falso
    }
    
    return render(request, 'perfil.html', contexto)