# app/schemas/produto_schema.py
from pydantic import BaseModel
from datetime import datetime

class ProdutoBase(BaseModel):
    nome: str
    quantidade: int
    descricao: str | None = None

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoOut(ProdutoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
