from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.produtor import Produtor
from schemas.produtor import ProdutorCreate

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
    produtor = await obter_produtor(db, produtor_id)
    if produtor:
        await db.delete(produtor)
        await db.commit()
        return True
    return False
