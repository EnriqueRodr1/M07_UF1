from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    partidas = relationship("RegistroPartida", back_populates="usuario")

class Palabra(Base):
    __tablename__ = 'palabras'
    id = Column(Integer, primary_key=True, index=True)
    palabra = Column(String, unique=True, index=True)

class RegistroPartida(Base):
    __tablename__ = 'registro_partidas'
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    palabra_id = Column(Integer, ForeignKey('palabras.id'))
    intentos = Column(Integer, default=0)
    errores = Column(Integer, default=0)
    fecha = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="partidas")
