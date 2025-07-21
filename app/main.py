from fastapi import FastAPI
from routers import produtores, propriedade, cultura_safra, dashboard
from database import create_db

app = FastAPI(title="Cadastro de Produtores Rurais")

app.include_router(produtores.router)
app.include_router(propriedade.router)
app.include_router(cultura_safra.router)
app.include_router(dashboard.router)

@app.on_event("startup")
async def startup_event():
    await create_db()

@app.get("/")
async def root():
    return {"message": "API está no ar!"}