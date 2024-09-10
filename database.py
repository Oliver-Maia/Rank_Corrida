from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///base.db')  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Corredor(Base):
    __tablename__ = 'corredores'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    idade = Column(Integer)
    sexo = Column(String)
    ativo = Column(Boolean)


Base.metadata.create_all(bind=engine)
