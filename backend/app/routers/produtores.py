from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas.produtor import ProdutorCreate, ProdutorRead
from crud import produtor as crud
from typing import List

router = APIRouter(prefix="/produtores", tags=["Produtores"])

@router.post("/", response_model=ProdutorRead)
async def criar_produtor(produtor: ProdutorCreate, db: AsyncSession = Depends(get_db)):
    return await crud.criar_produtor(db, produtor)

@router.get("/", response_model=List[ProdutorRead])
async def listar_produtores(db: AsyncSession = Depends(get_db)):
    return await crud.listar_produtores(db)

@router.get("/{produtor_id}", response_model=ProdutorRead)
async def obter_produtor(produtor_id: int, db: AsyncSession = Depends(get_db)):
    produtor = await crud.obter_produtor(db, produtor_id)
    if not produtor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produtor não encontrado")
    return produtor

@router.delete("/{produtor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_produtor(produtor_id: int, db: AsyncSession = Depends(get_db)):
    sucesso = await crud.deletar_produtor(db, produtor_id)
    if not sucesso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produtor não encontrado")
    return None
