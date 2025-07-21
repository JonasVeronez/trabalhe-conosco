from sqlalchemy import Column, String, Integer
from database import Base  

class Produtor(Base):
    __tablename__ = "produtores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    documento = Column(String, unique=True, nullable=False) 
    cidade = Column(String, nullable=False)
    estado = Column(String, nullable=False)
