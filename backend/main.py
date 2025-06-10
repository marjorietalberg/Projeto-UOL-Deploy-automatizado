from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import random
import httpx

app = FastAPI()

# Middleware para liberar CORS (cross-origin requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Se quiser limitar, especifique o domínio, ex: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint raiz — para testar se a API está rodando
@app.get("/")
async def root():
    return {"message": "API FastAPI rodando com sucesso!"}

# 1️⃣ Endpoint que retorna uma cor aleatória
@app.get("/color")
async def get_random_color():
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F333FF", "#33FFF3"]
    return {"color": random.choice(colors)}

# 2️⃣ Endpoint que retorna uma imagem aleatória de gato (usando API externa)
@app.get("/cat")
async def get_random_cat_image():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.thecatapi.com/v1/images/search")
        if response.status_code == 200:
            data = response.json()
            image_url = data[0]['url']
            return {"cat_image_url": image_url}
    return JSONResponse(content={"error": "Failed to fetch cat image"}, status_code=500)

# 3️⃣ Endpoint que retorna uma foto aleatória do Picsum
@app.get("/random-photo")
async def get_random_photo():
    width = random.randint(200, 600)
    height = random.randint(200, 600)
    photo_url = f"https://picsum.photos/{width}/{height}"
    return {"random_photo_url": photo_url}

# 4️⃣ Endpoint que retorna o horário atual
@app.get("/time")
async def get_current_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": now}

# 5️⃣ Endpoint que retorna imagens para "susto"
@app.get("/scare")
async def scare():
    scare_images = [
        "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
        "https://media.giphy.com/media/26xBI73gWquCBBCDe/giphy.gif"
    ]
    return {"scare_image_url": random.choice(scare_images)}

# 6️⃣ Endpoint que retorna imagens "parecidas"
@app.get("/lookalike")
async def lookalike():
    lookalike_images = [
        "https://randomuser.me/api/portraits/men/1.jpg",
        "https://randomuser.me/api/portraits/women/1.jpg",
        "https://randomuser.me/api/portraits/lego/1.jpg"
    ]
    return {"lookalike_image_url": random.choice(lookalike_images)}
