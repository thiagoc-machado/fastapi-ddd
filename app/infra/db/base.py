# app/infra/db/base.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# importa os modelos aqui
from app.infra.db.models import cliente_model, produto_model