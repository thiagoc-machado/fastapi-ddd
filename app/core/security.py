# app/core/security.py
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash_senha: str) -> bool:
    return pwd_context.verify(senha, hash_senha)
