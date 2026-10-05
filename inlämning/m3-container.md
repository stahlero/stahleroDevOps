M3 — Container
Dockerfiles
Granskade Dockerfiles och förutspådde deras funktion innan körning:

Backend: python:3.12-slim, installerar paket, kopierar applikation och tester, startar FastAPI via Uvicorn på port 8000.

Frontend: nginx, kopierar filer och konfiguration, exponerar port 8080.

Docker Compose
Byggde och startade med docker compose up --build. Båda containrarna startade och verifierades i webbläsaren på http://localhost:8080.

.dockerignore
Lade till .dockerignore i både backend/ och frontend/. Ändringarna granskades och sammanfogades via en pull-förfrågan.

GHCR
Taggade och skickade båda avbildningarna manuellt till GitHub Container Registry:

ghcr.io/stahlero/template-app-backend:latest

ghcr.io/stahlero/template-app-frontend:latest

Avbildningarna finns under repositoryts Packages.