from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# =========================
# USUÁRIOS
# =========================
class Usuario(Base):
    _tablename_ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(200), unique=True, index=True)
    senha_hash = Column(String(255), nullable=False)

    eh_artista = Column(Boolean, default=False)

    criado_em = Column(DateTime, default=datetime.utcnow)

    # RELACIONAMENTOS
    artista = relationship(
        "Artista",
        back_populates="usuario",
        uselist=False
    )

    carrinho = relationship(
        "Carrinho",
        back_populates="usuario",
        uselist=False
    )

    avaliacoes = relationship(
        "Avaliacao",
        back_populates="usuario"
    )

# =========================
# ARTISTAS
# =========================
class Artista(Base):
    _tablename_ = "artistas"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False
    )

    cidade = Column(String(100))
    estado = Column(String(2))
    bio = Column(Text)

    avatar_url = Column(String(500))
    banner_url = Column(String(500))

    facebook = Column(String(300))
    instagram = Column(String(300))
    discord = Column(String(300))
    twitter = Column(String(300))
    website = Column(String(300))

    # RELACIONAMENTOS
    usuario = relationship(
        "Usuario",
        back_populates="artista"
    )

    obras = relationship(
        "Obra",
        back_populates="artista"
    )


# =========================
# OBRAS
# =========================
class Obra(Base):
    _tablename_ = "obras"

    id = Column(Integer, primary_key=True, index=True)

    artista_id = Column(
        Integer,
        ForeignKey("artistas.id"),
        nullable=False
    )

    titulo = Column(String(200), nullable=False)

    descricao = Column(Text)

    preco = Column(Float, nullable=False)

    categoria = Column(String(50))
    # Ex: PINTURA, CERAMICA, DESENHO, FOTOGRAFIA

    estilo = Column(String(100))
    # Ex: ROCOCO

    image_url = Column(String(500))

    disponivel = Column(Boolean, default=True)

    criado_em = Column(DateTime, default=datetime.utcnow)

    # RELACIONAMENTOS
    artista = relationship(
        "Artista",
        back_populates="obras"
    )

    itens_carrinho = relationship(
        "ItemCarrinho",
        back_populates="obra"
    )

    avaliacoes = relationship(
        "Avaliacao",
        back_populates="obra"
    )


# =========================
# CARRINHO
# =========================
class Carrinho(Base):
    _tablename_ = "carrinhos"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(
        Integer,
        ForeignKey("usuarios.id"),
        unique=True,
        nullable=False
    )

    # RELACIONAMENTOS
    usuario = relationship(
        "Usuario",
        back_populates="carrinho"
    )

    itens = relationship(
        "ItemCarrinho",
        back_populates="carrinho",
        cascade="all, delete-orphan"
    )

# ===== ITENS DO CARRINHO =======
class ItemCarrinho(Base):
    __tablename__ = "itens_carrinho"

    id = Column(Integer, primary_key=True, index=True)

    carrinho_id = Column(
        Integer,
        ForeignKey("carrinhos.id"),
        nullable=False
    )

    obra_id = Column(
        Integer,
        ForeignKey("obras.id"),
        nullable=False
    )

    # RELACIONAMENTOS
    carrinho = relationship(
        "Carrinho",
        back_populates="itens"
    )

    obra = relationship(
        "Obra",
        back_populates="itens_carrinho"
    )

# ====== AVALIAÇÕES ======
class Avaliacao(Base):
    __tablename__ = "avaliacoes"

    id = Column(Integer, primary_key=True, index=True)

    obra_id = Column(
        Integer,
        ForeignKey("obras.id"),
        nullable=False
    )

    usuario_id = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False
    )

    nota = Column(Integer, nullable=False)

    comentario = Column(Text)

    criado_em = Column(DateTime, default=datetime.utcnow)

    # RELACIONAMENTOS
    obra = relationship(
        "Obra",
        back_populates="avaliacoes"
    )

    usuario = relationship(
        "Usuario",
        back_populates="avaliacoes"
    )