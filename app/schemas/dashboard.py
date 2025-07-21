from pydantic import BaseModel
from typing import List

class PropriedadePorEstado(BaseModel):
    estado: str
    quantidade: int
    percentual: float

class Cultura(BaseModel):
    nome: str
    quantidade: int
    percentual: float

class UsoSolo(BaseModel):
    agricultavel: float  # sem o u extra
    vegetacao: float
    percentual_agricultavel: float
    percentual_vegetacao: float
class DashboardResponse(BaseModel):
    total_fazendas: int
    total_hectares: float
    propriedades_por_estado: List[PropriedadePorEstado]
    culturas: List[Cultura]
    uso_solo: UsoSolo
