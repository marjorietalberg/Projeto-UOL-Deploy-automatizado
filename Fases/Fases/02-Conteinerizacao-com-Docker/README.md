<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=header" alt="Onda azul" />
</p>

# FASE 2: Docker e Docker Hub
### Objetivo:
- [x] Criar Dockerfile

- [x] Executar com Docker Compose (opcional)

- [x] Enviar para o Docker Hub
    
## 📌 1. Criar Dockerfile (exemplo para FastAPI):


# Dockerfile

```bash
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

```

## 📌 2. Testar com Docker Compose :
```bash

```
