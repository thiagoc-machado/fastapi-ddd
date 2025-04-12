# app/infra/db/models/produto_model.py
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.infra.db.base import Base

class ProdutoModel(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    descricao = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
