# IBRAAI

**Intelligent Business Research and Artificial Intelligence Platform**

IBRAAI is a Multi-Agent AI Ecosystem designed for Business Intelligence, Research Automation, Knowledge Management, and Enterprise Solutions.

---

## Features

### Backend (FastAPI)

* User Registration
* User Authentication (JWT)
* Password Hashing (bcrypt)
* SQLAlchemy Database Integration
* REST API Architecture
* Swagger Documentation

### Frontend

* Next.js
* TypeScript
* Responsive Dashboard
* Authentication UI

### Mobile

* Flutter Application
* Cross-platform Support
* User Authentication

### AI Layer

* Multi-Agent Architecture
* Research Agent
* Business Intelligence Agent
* Knowledge Agent
* Automation Agent

---

## Project Structure

```text
IBRAAI/
│
├── backend/
│   ├── app/
│   │   ├── auth.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── security.py
│   │   └── users.py
│   │
│   └── requirements.txt
│
├── frontend/
├── mobile/
├── docs/
├── infra/
│
├── README.md
├── LICENSE
└── .gitignore
```

---

## Backend Installation

### Install Dependencies

```bash
cd backend

pip install -r requirements.txt
```

### Run Server

```bash
uvicorn app.main:app --reload
```

### API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Authentication

### Register

```http
POST /register
```

Example:

```json
{
  "username": "admin",
  "email": "admin@example.com",
  "password": "password123"
}
```

### Login

```http
POST /login
```

Example:

```json
{
  "username": "admin",
  "password": "password123"
}
```

Response:

```json
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
```

---

## Technology Stack

* FastAPI
* SQLAlchemy
* SQLite
* JWT Authentication
* Passlib bcrypt
* Next.js
* Flutter
* Python

---

## License

MIT License

---

## Author

IBRAAI Development Team
