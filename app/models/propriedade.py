
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Propriedade(Base):
    __tablename__ = "propriedades"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    produtor_id = Column(Integer, ForeignKey("produtores.id"), nullable=False)

    produtor = relationship("Produtor", back_populates="propriedades")