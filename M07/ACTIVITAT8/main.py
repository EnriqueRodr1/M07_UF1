from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import get_db_connection

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    details: Optional[str] = None
    cost: float
    tax: Optional[float] = None
    available: bool
    category: str

@app.get("/")
def home():
    return {"message": "Welcome!"}

@app.get("/products/")
def list_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items;")
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"products": records}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items WHERE id = %s;", (product_id,))
    record = cursor.fetchone()
    cursor.close()
    conn.close()
    if record is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return record

@app.post("/products/")
def create_product(product: Product):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, description, price, tax, in_stock, category) VALUES (%s, %s, %s, %s, %s, %s);",
        (product.name, product.details, product.cost, product.tax, product.available, product.category),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Product added"}

@app.get("/health")
def health_check():
    return {"status": "Server is running"}
