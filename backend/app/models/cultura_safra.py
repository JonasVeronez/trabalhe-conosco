from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class CulturaSafra(Base):
    __tablename__ = "culturas_safra"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    variedade = Column(String, nullable=False)
    area_plantada = Column(Float, nullable=False)
    propriedade_id = Column(Integer, ForeignKey("propriedades.id"), nullable=False)

    propriedade = relationship("Propriedade", back_populates="culturas")
