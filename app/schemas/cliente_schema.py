# app/schemas/cliente_schema.py
from pydantic import BaseModel, EmailStr
from datetime import datetime

class ClienteBase(BaseModel):
    nome: str
    email: EmailStr

class ClienteCreate(ClienteBase):
    senha: str

class ClienteOut(ClienteBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
