
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas.propriedade import PropriedadeCreate, PropriedadeRead
from crud import propriedade as crud_propriedade
from typing import List

router = APIRouter(prefix="/propriedades", tags=["Propriedades"])

@router.post("/", response_model=PropriedadeRead)
async def criar_propriedade_endpoint(
    propriedade: PropriedadeCreate,
    db: AsyncSession = Depends(get_db),
):
    return await crud_propriedade.criar_propriedade(db, propriedade)


@router.get("/", response_model=List[PropriedadeRead])
async def listar_propriedades_endpoint(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    return await crud_propriedade.listar_propriedades(db, skip=skip, limit=limit)


@router.get("/{propriedade_id}", response_model=PropriedadeRead)
async def buscar_propriedade_endpoint(
    propriedade_id: int, db: AsyncSession = Depends(get_db)
):
    propriedade = await crud_propriedade.buscar_propriedade_por_id(db, propriedade_id)
    if not propriedade:
        raise HTTPException(status_code=404, detail="Propriedade não encontrada")
    return propriedade


@router.delete("/{propriedade_id}", status_code=204)
async def deletar_propriedade_endpoint(
    propriedade_id: int, db: AsyncSession = Depends(get_db)
):
    success = await crud_propriedade.deletar_propriedade(db, propriedade_id)
    if not success:
        raise HTTPException(status_code=404, detail="Propriedade não encontrada")