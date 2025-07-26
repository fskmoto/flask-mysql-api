PI de Produtos – Flask + MySQL + Docker Compose

API RESTful simples para cadastro e listagem de produtos, desenvolvida com Flask, persistência em banco de dados MySQL e orquestrada com Docker Compose.

---

## 🚀 Funcionalidades

- ✅ Listar todos os produtos (`GET /produtos`)
- ✅ Inserir novo produto (`POST /produtos`)
- 📌 Armazenamento persistente com MySQL
- 🔁 Containers isolados com Docker Compose

---

## 🧱 Tecnologias usadas

- Python 3.11
- Flask
- MySQL 5.7
- Docker + Docker Compose

---

## 📁 Estrutura do Projeto

---

## ⚙️ Como executar

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/flask-mysql-api.git
cd flask-mysql-api
docker-compose build
docker-compose up
curl -X POST http://localhost:5000/produtos \
  -H "Content-Type: application/json" \
  -d '{"nome": "Notebook", "preco": 4500.00}'
curl -X POST http://localhost:5000/produtos \
  -H "Content-Type: application/json" \
  -d '{"nome": "Notebook", "preco": 4500.00}'
curl http://localhost:5000/produtos

</details>

---

### 3. Salve e feche:

Se estiver usando `nano`:
- Pressione `Ctrl + O` (para salvar)
- Depois `Enter`
- Depois `Ctrl + X` (para sair)

---

### 4. Faça o commit:

```bash
git add README.md
git commit -m "Adiciona conteúdo completo ao README.md"
git push

</details>

---

### 3. Salve e feche:

Se estiver usando `nano`:
- Pressione `Ctrl + O` (para salvar)
- Depois `Enter`
- Depois `Ctrl + X` (para sair)

---

### 4. Faça o commit:

```bash
git add README.md
git commit -m "Adiciona conteúdo completo ao README.md"
git push
:wq!







