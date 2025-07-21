from pydantic import BaseModel, Field

class ProdutorBase(BaseModel):
    nome: str
    documento: str = Field(..., min_length=11, max_length=14)
    cidade: str
    estado: str

class ProdutorCreate(ProdutorBase):
    pass

class ProdutorRead(ProdutorBase):
    id: int

    class Config:
        from_attributes = True 
