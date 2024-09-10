from sqlalchemy.orm import Session
from database import SessionLocal, Corredor

def inserir_corredor(db: Session, nome: str, idade: int, sexo: bool, ativo: bool):
    sexo_str = 'Feminino' if sexo == 0 else 'Masculino'
    novo_corredor = Corredor(
        nome=nome,
        idade=idade,
        sexo=sexo_str,
        ativo=ativo
    )
    db.add(novo_corredor)
    db.commit()

def salvar_corredor(nome, idade, sexo, ativo):
    db_session = SessionLocal()
    try:
        inserir_corredor(db_session, nome, idade, sexo, ativo)
        print("Corredor salvo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar o corredor: {e}")
    finally:
        db_session.close()

