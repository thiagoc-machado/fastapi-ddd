# app/infra/repositories/produto_repo.py
from sqlalchemy.orm import Session
from app.infra.db.models.produto_model import ProdutoModel
from app.schemas.produto_schema import ProdutoCreate


class ProdutoRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: ProdutoCreate) -> ProdutoModel:
        db_produto = ProdutoModel(
            nome=produto.nome,
            quantidade=produto.quantidade,
            descricao=produto.descricao
        )
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar_todos(self) -> list[ProdutoModel]:
        return self.db.query(ProdutoModel).all()

    def buscar_por_id(self, id: int) -> ProdutoModel | None:
        return self.db.query(ProdutoModel).filter(ProdutoModel.id == id).first()
