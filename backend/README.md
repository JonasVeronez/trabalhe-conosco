# 🤞🌾 Cadastro de Produtores Rurais

Este projeto é uma API desenvolvida com **FastAPI** para o gerenciamento de:

* Produtores rurais
* Propriedades
* Culturas por safra
* Dashboard analítico de uso do solo

---

## 🚀 Como executar o projeto

### ✅ Pré-requisitos

* Python 3.12+
* PostgreSQL
* Docker (opcional para execução com container)

### 📦 Instalando dependências

```bash
pip install -r requirements.txt
```

### ▶️ Rodando localmente

```bash
uvicorn app.main:app --reload
```

Acesse:

* [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)
* [http://localhost:8000/redoc](http://localhost:8000/redoc) (ReDoc)

### 🐳 Usando Docker Compose

```bash
docker-compose up --build
```

---

## 📌 Principais Endpoints

* `POST /produtores/`
* `POST /propriedades/`
* `POST /cultura_safra/`
* `GET /dashboard/`

Documentação completa em: `/docs`

---

## 📏 Documentação OpenAPI

A documentação é gerada automaticamente pelo FastAPI:

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* OpenAPI JSON: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

---

## 🧠 Estrutura do Projeto

```
trabalhe-conosco/
├── app/
│   ├── core/            # Configurações e variáveis de ambiente
│   ├── crud/            # Funções de acesso ao banco
│   ├── models/          # Modelos do SQLAlchemy
│   ├── routers/         # Rotas da API
│   ├── schemas/         # Schemas do Pydantic
│   ├── database.py      # Conexão com o banco
│   └── main.py          # Inicialização da aplicação FastAPI
├── docker-compose.yml  # Subida com Docker
├── Dockerfile          # Dockerfile da API
├── requirements.txt    # Dependências do projeto
└── README.md
```

---

## 📊 Diagrama de Arquitetura

![Arquitetura](./docs/arquitetura.png)

> O diagrama representa a arquitetura baseada em FastAPI, PostgreSQL e separação por camadas (API, lógica e persistência).

---

## 👨‍💼 Autor

**Jonas Veronez**
[LinkedIn](https://www.linkedin.com/in/jonas-veronez-940887169/)
[jonassilva@gea.inatel.br]
---
