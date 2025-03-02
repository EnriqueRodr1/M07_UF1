from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from sqlalchemy.sql import func
import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Dependencia para obtener la BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Bienvenido al juego del ahorcado con FastAPI"}

# Endpoint para iniciar una partida
@app.post("/iniciar_partida/{usuario_id}")
def iniciar_partida(usuario_id: int, db: Session = Depends(get_db)):
    palabra = db.query(models.Palabra).order_by(func.random()).first()
    if not palabra:
        raise HTTPException(status_code=404, detail="No hay palabras disponibles")

    nueva_partida = models.RegistroPartida(usuario_id=usuario_id, palabra_id=palabra.id)
    db.add(nueva_partida)
    db.commit()
    return {"mensaje": "Partida iniciada", "palabra_id": palabra.id, "longitud": len(palabra.palabra)}

# Endpoint para intentar una letra
@app.post("/intento/{partida_id}/{letra}")
def intento(partida_id: int, letra: str, db: Session = Depends(get_db)):
    partida = db.query(models.RegistroPartida).filter(models.RegistroPartida.id == partida_id).first()
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")

    palabra = db.query(models.Palabra).filter(models.Palabra.id == partida.palabra_id).first().palabra

    if letra in palabra:
        return {"mensaje": "Letra correcta", "letra": letra}
    else:
        partida.errores += 1
        db.commit()
        return {"mensaje": "Letra incorrecta", "errores": partida.errores}

# Endpoint para obtener el abecedario
@app.get("/abecedario/")
def obtener_abecedario():
    return {"abecedario": list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

# Endpoint para obtener las estadísticas de un usuario
@app.get("/estadisticas/{usuario_id}")
def estadisticas(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    partidas_jugadas = len(usuario.partidas)
    partidas_ganadas = sum(1 for p in usuario.partidas if p.errores == 0)

    return {
        "usuario": usuario.nombre,
        "partidas_jugadas": partidas_jugadas,
        "partidas_ganadas": partidas_ganadas
    }
