# app/services/produto_service.py
from sqlalchemy.orm import Session
from app.schemas.produto_schema import ProdutoCreate
from app.infra.repositories.produto_repo import ProdutoRepository
from app.domain.produto import Produto

def criar_produto(db: Session, produto_data: ProdutoCreate):
    produto = Produto(
        nome=produto_data.nome,
        quantidade=produto_data.quantidade,
        descricao=produto_data.descricao or ''
    )
    repo = ProdutoRepository(db)
    return repo.criar(produto_data)

def listar_produtos(db: Session):
    repo = ProdutoRepository(db)
    return repo.listar_todos()

def buscar_produto_por_id(db: Session, id: int):
    repo = ProdutoRepository(db)
    return repo.buscar_por_id(id)
