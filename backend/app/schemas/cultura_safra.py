from pydantic import BaseModel, Field

class CulturaSafraBase(BaseModel):
    nome: str
    ano: int = Field(..., ge=2000, le=2100)
    variedade: str
    area_plantada: float = Field(..., gt=0)
    propriedade_id: int

class CulturaSafraCreate(CulturaSafraBase):
    pass

class CulturaSafraResponse(CulturaSafraBase):
    id: int

    class Config:
        from_attributes = True
