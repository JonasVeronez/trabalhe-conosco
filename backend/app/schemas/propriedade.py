from pydantic import BaseModel, Field, model_validator

class PropriedadeBase(BaseModel):
    nome: str
    cidade: str
    estado: str
    area_total: float = Field(..., gt=0)
    area_agricultavel: float = Field(..., ge=0)
    area_vegetacao: float = Field(..., ge=0)

    @model_validator(mode="after")
    def validar_areas(self) -> "PropriedadeBase":
        if self.area_agricultavel + self.area_vegetacao > self.area_total:
            raise ValueError("A soma da área agricultável e vegetação não pode exceder a área total")
        return self


class PropriedadeCreate(PropriedadeBase):
    produtor_id: int


class PropriedadeResponse(PropriedadeBase):
    id: int
    produtor_id: int

    class Config:
        from_attributes = True
