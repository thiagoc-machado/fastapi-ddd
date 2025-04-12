# app/domain/cliente.py
class Cliente:
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

    def atualizar_dados(self, nome: str, email: str):
        self.nome = nome
        self.email = email
