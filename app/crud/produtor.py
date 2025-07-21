from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.produtor import Produtor
from schemas.produtor import ProdutorCreate
from models.propriedade import Propriedade
from models.cultura_safra import CulturaSafra

async def criar_produtor(db: AsyncSession, produtor: ProdutorCreate):
    novo = Produtor(**produtor.dict())
    db.add(novo)
    await db.commit()
    await db.refresh(novo)
    return novo

async def listar_produtores(db: AsyncSession):
    result = await db.execute(select(Produtor))
    return result.scalars().all()

async def obter_produtor(db: AsyncSession, produtor_id: int):
    result = await db.execute(select(Produtor).where(Produtor.id == produtor_id))
    return result.scalars().first()

async def deletar_produtor(db: AsyncSession, produtor_id: int):
    produtor = await db.get(Produtor, produtor_id)
    if not produtor:
        return False

    # Buscar propriedades relacionadas ao produtor
    result = await db.execute(
        select(Propriedade).where(Propriedade.produtor_id == produtor_id)
    )
    propriedades = result.scalars().all()

    for prop in propriedades:
        # Buscar e deletar culturas relacionadas à propriedade
        culturas_result = await db.execute(
            select(CulturaSafra).where(CulturaSafra.propriedade_id == prop.id)
        )
        culturas = culturas_result.scalars().all()

        for cultura in culturas:
            await db.delete(cultura)

        # Deletar a propriedade após remover culturas
        await db.delete(prop)

    # Por fim, deletar o produtor
    await db.delete(produtor)
    await db.commit()
    return True