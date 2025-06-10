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
