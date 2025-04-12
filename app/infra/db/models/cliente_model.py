# app/infra/db/models/cliente_model.py
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.infra.db.base import Base

class ClienteModel(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
