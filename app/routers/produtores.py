from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db 
from schemas.produtor import ProdutorCreate, ProdutorRead 
from crud import produtor as crud 

router = APIRouter(prefix="/produtores", tags=["Produtores"])

@router.post("/", response_model=ProdutorRead)
async def criar_produtor(produtor: ProdutorCreate, db: AsyncSession = Depends(get_db)):
    return await crud.criar_produtor(db, produtor)

@router.get("/", response_model=list[ProdutorRead])
async def listar_produtores(db: AsyncSession = Depends(get_db)):
    return await crud.listar_produtores(db)
