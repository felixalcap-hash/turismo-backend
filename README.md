# 🌴 Turismo Backend

API REST para la gestión de ofertas turísticas y reservas.

## 📖 Descripción

Este proyecto proporciona los servicios necesarios para que la plataforma turística consulte ofertas y registre reservas en una base de datos MySQL alojada en Aiven.

## ✨ Funcionalidades

- Consultar ofertas turísticas
- Registrar reservas
- Consultar reservas
- Conexión con MySQL
- API REST con FastAPI
- Documentación automática con Swagger

## 🛠 Tecnologías Utilizadas

- Python
- FastAPI
- Uvicorn
- MySQL
- Aiven
- Poetry
- Render
- GitHub

## 📂 Estructura del Proyecto

```text
turismo-backend/
│
├── database.py
├── routes.py
├── main.py
├── crear_tablas.py
├── .env
├── pyproject.toml
└── poetry.lock
```

## ⚙️ Instalación

Clonar el repositorio:

```bash
git clone https://github.com/felixalcap-hash/turismo-backend.git
```

Entrar al proyecto:

```bash
cd turismo-backend
```

Instalar dependencias:

```bash
poetry install
```

Ejecutar localmente:

```bash
poetry run uvicorn main:app --reload
```

## 🔌 Endpoints

### Obtener ofertas

```http
GET /ofertas
```

### Obtener reservas

```http
GET /reservas
```

### Registrar reserva

```http
POST /reservas
```

Ejemplo:

```json
{
  "nombre": "Felix Alcantara",
  "correo": "felix@gmail.com",
  "telefono": "8090000000",
  "destino": "Isla Saona",
  "fecha": "2026-06-15",
  "personas": 2,
  "comentario": "Quiero más información"
}
```

## 🗄 Base de Datos

Motor:

```text
MySQL 8
```

Proveedor:

```text
Aiven Cloud
```

Tablas:

- ofertas
- reservas

## 📚 Documentación Swagger

https://turismo-backend-tg1w.onrender.com/docs

## 🌐 Despliegue

Backend desplegado en Render:

https://turismo-backend-tg1w.onrender.com

## 👨‍💻 Desarrollador

Proyecto académico desarrollado para la asignatura de Desarrollo Web.

**Autor:** Felix
