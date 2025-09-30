# FastAPI Modular Monolith

Dieses Projekt bietet ein Grundgerüst für einen modularen Monolithen mit FastAPI, Domain Driven Design und einem einfachen In-Process-Messagebus. Die Struktur ermöglicht die Trennung von Domänen, Application Layer, Infrastruktur und Präsentation.

## Features

- FastAPI mit orjson als Standard-Response
- SQLAlchemy 2.0 & Alembic für Datenbankzugriff und Migrationen
- Asynchrone PostgreSQL Treiber (asyncpg) und psycopg für Alembic
- Structlog für strukturierte Logs
- OIDC Hook mit Authlib und python-jose
- Redis & fastapi-limiter vorbereitet für spätere Ratenbegrenzung und Streams
- Tenancy Middleware über HTTP Header
- Einfacher Outbox-Worker als Platzhalter

## Entwicklung

```bash
make run        # startet die FastAPI App
make worker     # startet den Outbox Worker
make migrate    # führt Alembic Migrationen aus
```

## Docker

```bash
docker-compose up --build
```

Die Anwendung erwartet eine `.env` Datei basierend auf `.env.example`.
