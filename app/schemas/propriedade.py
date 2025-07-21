# app/schemas/propriedade.py

from pydantic import BaseModel
from typing import Optional


class PropriedadeBase(BaseModel):
    nome: str
    cidade: str
    estado: str
    produtor_id: int


class PropriedadeCreate(BaseModel):
    nome: str
    cidade: str
    estado: str
    produtor_id: int

class PropriedadeRead(PropriedadeCreate):
    id: int

    class Config:
        from_attributes = True
