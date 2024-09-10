from sqlalchemy import Column, ForeignKey, Integer, String, Date, Time, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Corredor(Base):
    __tablename__ = 'corredores'
    id_corredor = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    sexo = Column(String)
    ativo = Column(Integer)
    categoria_id = Column(Integer, ForeignKey('categorias.id_categoria'))

class Categoria(Base):
    __tablename__ = 'categorias'
    id_categoria = Column(Integer, primary_key=True)
    descricao = Column(String)
    faixa_etaria_inicial = Column(Integer)
    faixa_etaria_final = Column(Integer)

class Evento(Base):
    __tablename__= 'eventos'
    id_evento = Column(Integer, primary_key=True)
    nome_evento = Column(String)
    data = Column(Date)

class Resultado(Base):
    __tablename__ = 'resultados'
    id_resultado = Column (Integer, primary_key=True)
    id_evento = Column(Integer, ForeignKey('eventos.id_evento'))
    id_corredor = Column (Integer, ForeignKey('corredores.id_corredor'))
    tempo = Column(Time)
    id_categoria = Column(Integer, ForeignKey('categorias.id_categoria'))
    posicao = Column (Integer)
    classificacao = Column (Integer)

