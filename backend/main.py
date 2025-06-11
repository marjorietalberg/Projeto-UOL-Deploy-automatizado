from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import random
import httpx

app = FastAPI(
    title="API FastAPI Hello",
    description="API simples com vários endpoints para cores, imagens, tempo e mais",
    version="1.0.0",
)

# Middleware para liberar CORS (cross-origin requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Para produção, restrinja os domínios!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", summary="Raiz", tags=["Geral"])
async def root():
    """Endpoint raiz para testar se a API está rodando"""
    return {"message": "API FastAPI rodando com sucesso!"}

@app.get("/color", summary="Cor Aleatória", tags=["Utilitários"])
async def get_random_color():
    """Retorna uma cor hexadecimal aleatória"""
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F333FF", "#33FFF3"]
    return {"color": random.choice(colors)}

@app.get("/cat", summary="Imagem Aleatória de Gato", tags=["Imagens"])
async def get_random_cat_image():
    """Consulta API externa para retornar uma imagem aleatória de gato"""
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.thecatapi.com/v1/images/search")
        if response.status_code == 200:
            data = response.json()
            return {"cat_image_url": data[0]["url"]}
    return JSONResponse(content={"error": "Failed to fetch cat image"}, status_code=500)

@app.get("/random-photo", summary="Foto Aleatória", tags=["Imagens"])
async def get_random_photo():
    """Retorna URL de foto aleatória com dimensões variáveis"""
    width = random.randint(200, 600)
    height = random.randint(200, 600)
    url = f"https://picsum.photos/{width}/{height}"
    return {"random_photo_url": url}

@app.get("/time", summary="Hora Atual", tags=["Utilitários"])
async def get_current_time():
    """Retorna a data e hora atual formatada"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": now}

@app.get("/scare", summary="Imagem de Susto", tags=["Imagens"])
async def scare():
    """Retorna imagem aleatória para 'susto'"""
    images = [
        "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
        "https://media.giphy.com/media/26xBI73gWquCBBCDe/giphy.gif",
    ]
    return {"scare_image_url": random.choice(images)}

@app.get("/lookalike", summary="Imagens Parecidas", tags=["Imagens"])
async def lookalike():
    """Retorna imagem aleatória de pessoas parecidas"""
    images = [
        "https://randomuser.me/api/portraits/men/1.jpg",
        "https://randomuser.me/api/portraits/women/1.jpg",
        "https://randomuser.me/api/portraits/lego/1.jpg",
    ]
    return {"lookalike_image_url": random.choice(images)}
