# app/api/v1/clientes.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.cliente_schema import ClienteCreate, ClienteOut
from app.services.cliente_service import criar_cliente, listar_clientes, buscar_cliente_por_id
from app.api.deps import get_db

router = APIRouter()

@router.post('/', response_model=ClienteOut, status_code=status.HTTP_201_CREATED)
def criar(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return criar_cliente(db, cliente)

@router.get('/', response_model=list[ClienteOut])
def listar(db: Session = Depends(get_db)):
    return listar_clientes(db)

@router.get('/{id}', response_model=ClienteOut)
def buscar(id: int, db: Session = Depends(get_db)):
    return buscar_cliente_por_id(db, id)
