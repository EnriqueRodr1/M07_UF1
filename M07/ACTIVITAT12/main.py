from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
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

# ==================== CRUD USUARIOS ====================
@app.post("/usuarios/")
def crear_usuario(nombre: str, db: Session = Depends(get_db)):
    nuevo_usuario = models.Usuario(nombre=nombre)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.get("/usuarios/")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()

@app.put("/usuarios/{usuario_id}")
def actualizar_usuario(usuario_id: int, nombre: str, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario.nombre = nombre
    db.commit()
    return usuario

@app.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario)
    db.commit()
    return {"mensaje": "Usuario eliminado correctamente"}

# ==================== CRUD PALABRAS ====================
@app.post("/palabras/")
def crear_palabra(palabra: str, db: Session = Depends(get_db)):
    nueva_palabra = models.Palabra(palabra=palabra)
    db.add(nueva_palabra)
    db.commit()
    db.refresh(nueva_palabra)
    return nueva_palabra

@app.get("/palabras/{palabra_id}")
def obtener_palabra(palabra_id: int, db: Session = Depends(get_db)):
    palabra = db.query(models.Palabra).filter(models.Palabra.id == palabra_id).first()
    if not palabra:
        raise HTTPException(status_code=404, detail="Palabra no encontrada")
    return palabra

@app.get("/palabras/")
def listar_palabras(db: Session = Depends(get_db)):
    return db.query(models.Palabra).all()

@app.put("/palabras/{palabra_id}")
def actualizar_palabra(palabra_id: int, nueva_palabra: str, db: Session = Depends(get_db)):
    palabra = db.query(models.Palabra).filter(models.Palabra.id == palabra_id).first()
    if not palabra:
        raise HTTPException(status_code=404, detail="Palabra no encontrada")
    palabra.palabra = nueva_palabra
    db.commit()
    return palabra

@app.delete("/palabras/{palabra_id}")
def eliminar_palabra(palabra_id: int, db: Session = Depends(get_db)):
    palabra = db.query(models.Palabra).filter(models.Palabra.id == palabra_id).first()
    if not palabra:
        raise HTTPException(status_code=404, detail="Palabra no encontrada")
    db.delete(palabra)
    db.commit()
    return {"mensaje": "Palabra eliminada correctamente"}

# ==================== CRUD REGISTRO PARTIDAS ====================
@app.post("/registro_partidas/")
def crear_registro_partida(usuario_id: int, palabra_id: int, db: Session = Depends(get_db)):
    nueva_partida = models.RegistroPartida(usuario_id=usuario_id, palabra_id=palabra_id)
    db.add(nueva_partida)
    db.commit()
    db.refresh(nueva_partida)
    return nueva_partida

@app.get("/registro_partidas/{partida_id}")
def obtener_registro_partida(partida_id: int, db: Session = Depends(get_db)):
    partida = db.query(models.RegistroPartida).filter(models.RegistroPartida.id == partida_id).first()
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    return partida

@app.get("/registro_partidas/")
def listar_registro_partidas(db: Session = Depends(get_db)):
    return db.query(models.RegistroPartida).all()

@app.put("/registro_partidas/{partida_id}")
def actualizar_registro_partida(partida_id: int, intentos: int, errores: int, db: Session = Depends(get_db)):
    partida = db.query(models.RegistroPartida).filter(models.RegistroPartida.id == partida_id).first()
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    partida.intentos = intentos
    partida.errores = errores
    db.commit()
    return partida

@app.delete("/registro_partidas/{partida_id}")
def eliminar_registro_partida(partida_id: int, db: Session = Depends(get_db)):
    partida = db.query(models.RegistroPartida).filter(models.RegistroPartida.id == partida_id).first()
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    db.delete(partida)
    db.commit()
    return {"mensaje": "Registro de partida eliminado correctamente"}
