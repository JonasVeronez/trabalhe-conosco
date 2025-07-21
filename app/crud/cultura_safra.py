from models.cultura_safra import CulturaSafra
from schemas.cultura_safra import CulturaSafraCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

async def criar_cultura_safra(db: AsyncSession, cultura: CulturaSafraCreate):
    nova = CulturaSafra(**cultura.model_dump())
    db.add(nova)
    await db.commit()
    await db.refresh(nova)
    return nova

async def listar_culturas_safra(db: AsyncSession):
    result = await db.execute(select(CulturaSafra))
    return result.scalars().all()

async def obter_cultura_safra(db: AsyncSession, cultura_id: int):
    result = await db.execute(select(CulturaSafra).where(CulturaSafra.id == cultura_id))
    return result.scalar_one_or_none()

async def deletar_cultura_safra(db: AsyncSession, cultura_id: int) -> bool:
    cultura = await db.get(CulturaSafra, cultura_id)
    if cultura:
        await db.delete(cultura)
        await db.commit()
        return True
    return False