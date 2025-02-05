from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Word
from schemas import ThemeOption, WordOption
import random

app = FastAPI()

# Ruta raíz
@app.get("/")
def read_root():
    return {"message": "Welcome to the Penjat API!"}

@app.get("/penjat/tematica/opcions", response_model=list[ThemeOption])
async def get_themes(db: Session = Depends(get_db)):
    themes = db.query(Word.theme).distinct().all()
    if not themes:
        raise HTTPException(status_code=404, detail="No themes found")
    return [{"option": theme[0]} for theme in themes]

@app.get("/penjat/tematica/{option}", response_model=list[WordOption])
async def get_word_by_theme(option: str, db: Session = Depends(get_db)):
    words = db.query(Word.word).filter(Word.theme == option).all()
    if not words:
        raise HTTPException(status_code=404, detail=f"No words found for theme: {option}")
    random_word = random.choice(words)
    return [{"option": random_word.word}]
