from sqlalchemy import select, func
from models.propriedade import Propriedade
from models.cultura_safra import CulturaSafra
from sqlalchemy.ext.asyncio import AsyncSession

async def obter_dashboard(db: AsyncSession):
    total_fazendas = await db.scalar(select(func.count(Propriedade.id)))

    total_hectares = await db.scalar(select(func.coalesce(func.sum(Propriedade.area_total), 0)))

    propriedades_por_estado_res = await db.execute(
        select(
            Propriedade.estado,
            func.count(Propriedade.id).label("quantidade")
        ).group_by(Propriedade.estado)
    )
    propriedades_por_estado = propriedades_por_estado_res.all()

    culturas_res = await db.execute(
        select(
            CulturaSafra.nome,
            func.count(CulturaSafra.id).label("quantidade"),
            func.coalesce(func.sum(CulturaSafra.area_plantada), 0).label("area_plantada")
        ).group_by(CulturaSafra.nome)
    )
    culturas = culturas_res.all()

    uso_solo_res = await db.execute(
        select(
            func.coalesce(func.sum(Propriedade.area_agricultavel), 0).label("agricultavel"),
            func.coalesce(func.sum(Propriedade.area_vegetacao), 0).label("vegetacao")
        )
    )
    uso_solo = uso_solo_res.first()

    total_uso_solo = (uso_solo.agricultavel or 0) + (uso_solo.vegetacao or 0)
    if total_uso_solo == 0:
        total_uso_solo = 1  # para evitar divisão por zero

    return {
        "total_fazendas": total_fazendas,
        "total_hectares": float(total_hectares or 0),
        "propriedades_por_estado": [
            {
                "estado": estado,
                "quantidade": qtd,
                "percentual": round(qtd / total_fazendas * 100, 2) if total_fazendas else 0
            }
            for estado, qtd in propriedades_por_estado
        ],
        "culturas": [
            {
                "nome": nome,
                "quantidade": qtd,
                "percentual": round(area_plantada / total_hectares * 100, 2) if total_hectares else 0
            }
            for nome, qtd, area_plantada in culturas
        ],
        "uso_solo": {
            "agricultavel": float(uso_solo.agricultavel),
            "vegetacao": float(uso_solo.vegetacao),
            "percentual_agricultavel": round(uso_solo.agricultavel / total_uso_solo * 100, 2),
            "percentual_vegetacao": round(uso_solo.vegetacao / total_uso_solo * 100, 2),
        }
    }
