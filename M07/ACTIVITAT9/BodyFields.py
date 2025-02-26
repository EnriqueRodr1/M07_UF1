from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated, Optional

app = FastAPI()

class Articulo(BaseModel):
    titulo: str
    resumen: Optional[str] = Field(
        default=None, title="Resumen del artículo", max_length=500
    )
    precio: float = Field(gt=0, description="El precio debe ser un número positivo")
    tasa_impuesto: Optional[float] = None

@app.put("/articulos/{id_articulo}")
async def actualizar_articulo(id_articulo: int, articulo: Annotated[Articulo, Body(embed=True)]):
    respuesta = {"id_articulo": id_articulo, "articulo": articulo}
    return respuesta
