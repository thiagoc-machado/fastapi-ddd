# app/services/cliente_service.py
from sqlalchemy.orm import Session
from app.schemas.cliente_schema import ClienteCreate
from app.infra.repositories.cliente_repo import ClienteRepository
from app.domain.cliente import Cliente

def criar_cliente(db: Session, cliente_data: ClienteCreate):
    cliente = Cliente(
        nome=cliente_data.nome,
        email=cliente_data.email,
        senha=cliente_data.senha
    )
    repo = ClienteRepository(db)
    return repo.criar(cliente_data)

def listar_clientes(db: Session):
    repo = ClienteRepository(db)
    return repo.listar_todos()

def buscar_cliente_por_id(db: Session, id: int):
    repo = ClienteRepository(db)
    return repo.buscar_por_id(id)
