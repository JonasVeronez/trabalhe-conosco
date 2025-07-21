from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.produtor import Produtor
from schemas.produtor import ProdutorCreate

async def criar_produtor(db: AsyncSession, produtor: ProdutorCreate):
    db_produtor = Produtor(**produtor.model_dump())
    db.add(db_produtor)
    await db.commit()
    await db.refresh(db_produtor)
    return db_produtor

async def listar_produtores(db: AsyncSession):
    result = await db.execute(select(Produtor))
    return result.scalars().all()
