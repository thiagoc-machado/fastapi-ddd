# app/infra/repositories/cliente_repo.py
from sqlalchemy.orm import Session
from app.infra.db.models.cliente_model import ClienteModel
from app.schemas.cliente_schema import ClienteCreate
from app.core.security import hash_senha

class ClienteRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, cliente: ClienteCreate) -> ClienteModel:
        db_cliente = ClienteModel(
            nome=cliente.nome,
            email=cliente.email,
            senha=hash_senha(cliente.senha)
        )
        self.db.add(db_cliente)
        self.db.commit()
        self.db.refresh(db_cliente)
        return db_cliente

    def listar_todos(self) -> list[ClienteModel]:
        return self.db.query(ClienteModel).all()

    def buscar_por_id(self, id: int) -> ClienteModel | None:
        return self.db.query(ClienteModel).filter(ClienteModel.id == id).first()
