import email
from database import SessaoLocal, engine, Base
import models
from auth_utils import hash_senha 

Base.metadata.createall(bind=engine)
db = SessaoLocal()

def popular():
    # Limpa tabelas na ordem certa
    db.query(models.Avaliacao).delete()
    db.query(models.ItemCarrinho).delete()
    db.query(models.Carrinho).delete()
    db.query(models.Obra).delete()
    db.query(models.Artista).delete()
    db.query(models.Usuario).delete()
    db.commit()

    # ----- Usuários / Artistas ---------------
    dados_artistas = [
        {
            "usuario": {"nome": "Analice Bittencourt", "email": "analice@email.com"},
            "perfil":  {"cidade": "São Paulo", "estado": "SP",
                        "bio": "Prepare-se para a ver as melhores obras de arte da sua vida!"},
        },
        {
            "usuario": {"nome": "Carlos Lima", "email": "carlos@email.com"},
            "perfil":  {"cidade": "Belo Horizonte", "estado": "MG", "bio": "Artista mineiro."},
        },
        {
            "usuario": {"nome": "Marina Costa", "email": "marina@email.com"},
            "perfil":  {"cidade": "Curitiba", "estado": "PR", "bio": "Cerâmica e escultura."},
        },
        {
            "usuario": {"nome": "Pedro Alves", "email": "pedro@email.com"},
            "perfil":  {"cidade": "Rio de Janeiro", "estado": "RJ", "bio": "Desenho e ilustração."},
        },
        {
            "usuario": {"nome": "David Aguiar", "email": "david@email.com"},
            "perfil":  {"cidade": "São Paulo", "estado": "SP", "bio": "Fotografia urbana."},
        },
        {
            "usuario": {"nome": "Ana Rodrigues", "email": "ana@email.com"},
            "perfil":  {"cidade": "São Paulo", "estado": "SP", "bio": "Pinturas abstratas."},
        },
    ]

    artistas_criados = []
    for dados in dados_artistas:
        usuario = models.Usuario(
            nome = dados['usuario']['nome'],
            email = dados['usuario']['email'],
            senha_hash = hash_senha('senha123'),
            eh_artista = True,
        )
        db.add(usuario)
        db.flush()

        artista = models.Artista(usuario_id=usuario.id, **dados['perfil'])
        db.add(artista)
        db.flush()
        artistas_criados.append(artista)

        carrinho = models.Carrinho