import pandas as pd
from sqlalchemy.orm import Session
from database import engine, Base
from models import Word

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Leer datos del archivo CSV
def insert_data():
    df = pd.read_csv("data.csv")  # Asegúrate de que el CSV tiene columnas: 'word' y 'theme'
    with Session(engine) as session:
        for _, row in df.iterrows():
            word = Word(word=row["word"], theme=row["theme"])
            session.add(word)
        session.commit()
        print(f"Se han insertado {len(df)} palabras en la base de datos.")

if __name__ == "__main__":
    insert_data()
