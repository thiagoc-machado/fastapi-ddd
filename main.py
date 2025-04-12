# app/main.py
from fastapi import FastAPI
from app.api.v1 import clientes, produtos

app = FastAPI()

app.include_router(clientes.router, prefix='/api/v1/clientes', tags=['Clientes'])
app.include_router(produtos.router, prefix='/api/v1/produtos', tags=['Produtos'])
