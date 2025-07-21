from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.propriedade import Propriedade
from models.cultura_safra import CulturaSafra

from schemas.propriedade import PropriedadeCreate


async def criar_propriedade(db: AsyncSession, propriedade: PropriedadeCreate) -> Propriedade:
    db_propriedade = Propriedade(**propriedade.dict())
    db.add(db_propriedade)
    await db.commit()
    await db.refresh(db_propriedade)
    return db_propriedade


async def listar_propriedades(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Propriedade).offset(skip).limit(limit))
    return result.scalars().all()


async def buscar_propriedade_por_id(db: AsyncSession, propriedade_id: int):
    result = await db.execute(select(Propriedade).where(Propriedade.id == propriedade_id))
    return result.scalar_one_or_none()


async def deletar_propriedade(db: AsyncSession, propriedade_id: int):

    propriedade = await db.get(Propriedade, propriedade_id)
    if not propriedade:
        return False


    culturas_result = await db.execute(
        select(CulturaSafra).where(CulturaSafra.propriedade_id == propriedade_id)
    )
    culturas = culturas_result.scalars().all()

    for cultura in culturas:
        await db.delete(cultura)

    await db.delete(propriedade)
    await db.commit()
    return True