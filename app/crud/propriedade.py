from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.propriedade import Propriedade
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


async def deletar_propriedade(db: AsyncSession, propriedade_id: int) -> bool:
    propriedade = await buscar_propriedade_por_id(db, propriedade_id)
    if propriedade:
        await db.delete(propriedade)
        await db.commit()
        return True
    return False