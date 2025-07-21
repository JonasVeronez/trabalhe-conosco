from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas.cultura_safra import CulturaSafraCreate, CulturaSafraResponse
from crud import cultura_safra as crud
from typing import List

router = APIRouter(prefix="/culturasafra", tags=["Cultura Safra"])

@router.post("/", response_model=CulturaSafraResponse)
async def criar(cultura: CulturaSafraCreate, db: AsyncSession = Depends(get_db)):
    return await crud.criar_cultura_safra(db, cultura)

@router.get("/", response_model=List[CulturaSafraResponse])
async def listar(db: AsyncSession = Depends(get_db)):
    return await crud.listar_culturas_safra(db)

@router.get("/{cultura_id}", response_model=CulturaSafraResponse)
async def obter(cultura_id: int, db: AsyncSession = Depends(get_db)):
    cultura = await crud.obter_cultura_safra(db, cultura_id)
    if not cultura:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cultura não encontrada")
    return cultura

@router.delete("/{cultura_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar(cultura_id: int, db: AsyncSession = Depends(get_db)):
    sucesso = await crud.deletar_cultura_safra(db, cultura_id)
    if not sucesso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cultura não encontrada")
    return None
