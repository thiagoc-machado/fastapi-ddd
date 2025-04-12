# app/api/v1/produtos.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.produto_schema import ProdutoCreate, ProdutoOut
from app.services.produto_service import criar_produto, listar_produtos, buscar_produto_por_id
from app.api.deps import get_db

router = APIRouter()

@router.post('/', response_model=ProdutoOut, status_code=status.HTTP_201_CREATED)
def criar(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return criar_produto(db, produto)

@router.get('/', response_model=list[ProdutoOut])
def listar(db: Session = Depends(get_db)):
    return listar_produtos(db)

@router.get('/{id}', response_model=ProdutoOut)
def buscar(id: int, db: Session = Depends(get_db)):
    return buscar_produto_por_id(db, id)
