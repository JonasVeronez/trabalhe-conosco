from sqlalchemy import Column, String, Integer
from database import Base  
from sqlalchemy.orm import relationship

class Produtor(Base):
    __tablename__ = "produtores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    documento = Column(String, nullable=False, unique=True)
    cidade = Column(String, nullable=False)
    estado = Column(String, nullable=False)

    propriedades = relationship("Propriedade", back_populates="produtor")