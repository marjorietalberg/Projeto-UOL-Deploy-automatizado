<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=header" alt="Onda azul" />
</p>

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" alt="Docker Icon" width="120" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://img.icons8.com/ios-filled/150/0078D7/parcel.png" alt="Container Icon" width="120" />
</p>


# FASE 2: Docker e Docker Hub
### Objetivo:
- [x] Criar Dockerfile

- [x] Executar com Docker Compose (opcional)

- [x] Enviar para o Docker Hub
    
## 📌 1. Criar Dockerfile (exemplo para FastAPI):


# Dockerfile

```bash
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas o arquivo de dependências para otimizar o cache
COPY requirements.txt .

# Atualiza pip e instala dependências (use --no-cache-dir para reduzir tamanho)
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia todo o restante do código para o container
COPY . .

# Expõe a porta 8000 para acesso externo
EXPOSE 8000

# Comando para iniciar a aplicação FastAPI com reload desativado (prod)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 📌 2. Testar com Docker Compose :
```bash

```
