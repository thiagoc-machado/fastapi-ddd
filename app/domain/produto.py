# app/domain/produto.py
class Produto:
    def __init__(self, nome: str, quantidade: int, descricao: str = ''):
        self.nome = nome
        self.quantidade = quantidade
        self.descricao = descricao

    def atualizar(self, nome: str, quantidade: int, descricao: str):
        self.nome = nome
        self.quantidade = quantidade
        self.descricao = descricao
