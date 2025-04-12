# 📦 FastAPI + SQLAlchemy + Alembic com DDD

Este projeto é uma aplicação FastAPI simples com banco de dados SQLite, organizada seguindo os princípios do **Domain-Driven Design (DDD)**. Possui duas entidades: `Cliente` e `Produto`.

---

📦 ESTRUTURA GERAL (seguindo DDD adaptado ao FastAPI)
✅ main.py
Responsável por: iniciar a aplicação FastAPI e registrar as rotas.

Por que existe: é o ponto de entrada da aplicação.

No DDD: conecta a camada de apresentação (API) com os casos de uso.

1️⃣ CAMADA DE APRESENTAÇÃO → app/api/
📁 api/v1/clientes.py e produtos.py
Responsável por: definir as rotas (endpoints REST).

Por que existe: separa a camada HTTP da lógica de negócio.

No DDD: é o Controller, mas não tem lógica de negócio — só recebe, chama e devolve.

📁 api/deps.py
Responsável por: fornecer a sessão do banco com Depends.

Por que existe: simplifica a injeção de dependências (como o DB).

No DDD: suporte técnico à camada de apresentação.

2️⃣ CAMADA DE DOMÍNIO → app/domain/
📄 cliente.py e produto.py
Responsável por: conter regras centrais do negócio.

Por que existe: representa as entidades com comportamento (métodos).

No DDD: é o coração da aplicação. Se a regra mudar, muda aqui.

3️⃣ CAMADA DE APLICAÇÃO → app/services/
📄 cliente_service.py e produto_service.py
Responsável por: orquestrar ações do domínio + repositório.

Por que existe: implementar casos de uso (ex: criar cliente, listar produtos).

No DDD: representa os Application Services — chamam domínio e persistência.

4️⃣ CAMADA DE INFRAESTRUTURA → app/infra/
📁 db/session.py
Responsável por: conexão com o banco (SQLite).

No DDD: infraestrutura de persistência, sem regra de negócio.

📁 db/base.py
Responsável por: base do SQLAlchemy, usada pelo Alembic.

No DDD: serve de suporte técnico à persistência.

📁 db/models/cliente_model.py e produto_model.py
Responsável por: definir a estrutura das tabelas no banco.

Por que existe: mapeamento ORM (modelos de dados).

No DDD: são Modelos de Persistência, não são os mesmos que o domínio.

📁 repositories/cliente_repo.py e produto_repo.py
Responsável por: fazer o CRUD real no banco.

Por que existe: abstrai a persistência.

No DDD: é o Repository Pattern — o domínio não conhece SQL!

5️⃣ CAMADA DE DTOs / TRANSFERÊNCIA → app/schemas/
📄 cliente_schema.py e produto_schema.py
Responsável por: validar e serializar os dados de entrada e saída.

Por que existe: desacopla o modelo de domínio do modelo da API.

No DDD: são os DTOs (Data Transfer Objects).

6️⃣ SEGURANÇA → app/core/security.py
Responsável por: hash e verificação de senhas.

Por que existe: centraliza regras de segurança.

No DDD: pode ser considerado um serviço de domínio técnico (externo ao core).

🧠 RESUMO SIMPLIFICADO DO FLUXO
Usuário envia dados via API (api/)

API chama um caso de uso (services/)

O caso de uso cria entidade (domain/) e usa o repositório (infra/) para salvar

Resposta é serializada com um schema (schemas/) e devolvida

## 🧱 Estrutura do Projeto

```
app/
├── api/                # Camada de apresentação (rotas FastAPI)
│   ├── deps.py
│   └── v1/
│       ├── clientes.py
│       └── produtos.py
├── core/               # Segurança e configurações
│   └── security.py
├── domain/             # Entidades e regras de negócio
│   ├── cliente.py
│   └── produto.py
├── infra/              # Infraestrutura: banco, models e repositórios
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── models/
│   │       ├── cliente_model.py
│   │       └── produto_model.py
│   └── repositories/
│       ├── cliente_repo.py
│       └── produto_repo.py
├── schemas/            # DTOs para entrada e saída de dados
│   ├── cliente_schema.py
│   └── produto_schema.py
├── services/           # Casos de uso (lógica da aplicação)
│   ├── cliente_service.py
│   └── produto_service.py
└── main.py             # Ponto de entrada da aplicação
```

---

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2. Crie o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

---

## 🛠️ Banco de dados

### 1. Inicialize o Alembic
```bash
alembic init alembic
```

### 2. Configure `alembic.ini` para SQLite
```ini
sqlalchemy.url = sqlite:///./db.sqlite3
```

### 3. Crie as tabelas
```bash
alembic revision --autogenerate -m "create clientes e produtos"
alembic upgrade head
```

---

## ▶️ Execução

```bash
uvicorn app.main:app --reload
```

Acesse: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Testes manuais

### Criar um cliente:
```http
POST /api/v1/clientes/
{
  "nome": "Thiago",
  "email": "thiago@example.com",
  "senha": "senha123"
}
```

### Criar um produto:
```http
POST /api/v1/produtos/
{
  "nome": "Camiseta",
  "quantidade": 10,
  "descricao": "Camiseta preta tamanho M"
}
```

---

## 🧠 Sobre o DDD usado

- **domain/** → entidades e regras de negócio (sem SQL ou FastAPI)
- **infra/** → acesso ao banco (models e repositórios)
- **services/** → casos de uso (lógica da aplicação)
- **schemas/** → entrada e saída de dados (DTOs)
- **api/** → rotas da aplicação

---

## 🛡 Segurança
A senha do cliente é criptografada com `bcrypt` via `passlib`.

---

## 📄 Licença
MIT
