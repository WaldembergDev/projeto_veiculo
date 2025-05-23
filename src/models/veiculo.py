from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from src.database.db import Base
import enum

class Status(str, enum.Enum):
  ATIVO = 'ativo'
  INATIVO = 'inativo'

class Veiculo(Base):
  __tablename__ = 'veiculos'
  
  id = Column(Integer, primary_key=True, unique= True)
  placa = Column(String(7), nullable=False)
  modelo = Column(String(120), nullable=False)
  cor = Column(String(50), nullable=False)
  odometro = Column(Integer(), nullable=False)
  avariado = Column(Boolean, nullable=False)
  status = Column(Enum(Status), default=Status.ATIVO, nullable=False)

  