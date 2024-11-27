from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import get_db_connection  # Importar la función de conexión

# Crear la aplicación FastAPI
app = FastAPI()

# Modelo de datos con BaseModel
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    in_stock: bool
    category: str

# Rutas y endpoints

@app.get("/")
def read_root():
    """Endpoint raíz"""
    return {"message": "Hello, World!"}

@app.get("/items/")
def get_items():
    """Endpoint GET para obtener todos los ítems de la tabla"""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items;")
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"items": items}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    """Endpoint GET para obtener un ítem específico"""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items WHERE id = %s;", (item_id,))
    item = cursor.fetchone()
    cursor.close()
    conn.close()
    if item is None:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return item

@app.post("/items/")
def create_item(item: Item):
    """Endpoint POST para crear un ítem"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO items (name, description, price, tax, in_stock, category)
        VALUES (%s, %s, %s, %s, %s, %s);
        """,
        (item.name, item.description, item.price, item.tax, item.in_stock, item.category),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Item creado!"}

@app.get("/status")
def check_status():
    """Endpoint adicional para probar el estado del servidor"""
    return {"status": "El servidor está en funcionamiento"}
