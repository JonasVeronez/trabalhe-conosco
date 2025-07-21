from fastapi import FastAPI
from routers import produtores  
from database import create_db  

app = FastAPI(title="Cadastro de Produtores Rurais")

app.include_router(produtores.router)

@app.on_event("startup")
async def startup_event():
    await create_db()

@app.get("/")
async def root():
    return {"message": "API está no ar!"}
