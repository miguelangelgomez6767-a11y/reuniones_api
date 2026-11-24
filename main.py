
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

import models
import schemas

from database import engine, get_db

# Crear las tablas
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Gestión de Reuniones")


# 1. REGISTRAR UNA REUNIÓN
@app.post("/reuniones/", response_model=schemas.ReunionResponse)
def crear_reunion(
    reunion: schemas.ReunionCreate,
    db: Session = Depends(get_db)
):

    nueva_reunion = models.Reunion(**reunion.model_dump())

    db.add(nueva_reunion)
    db.commit()
    db.refresh(nueva_reunion)

    return nueva_reunion


# 2. CONSULTAR TODAS LAS REUNIONES
# 5. FILTRAR REUNIONES POR FECHA
@app.get("/reuniones/", response_model=list[schemas.ReunionResponse])
def consultar_reuniones(
    fecha: date | None = None,
    db: Session = Depends(get_db)
):

    consulta = db.query(models.Reunion)

    if fecha is not None:
        consulta = consulta.filter(models.Reunion.fecha == fecha)

    return consulta.all()


# 3. CONSULTAR UNA REUNIÓN POR ID
@app.get("/reuniones/{id}", response_model=schemas.ReunionResponse)
def consultar_reunion(id: int, db: Session = Depends(get_db)):

    reunion = db.query(models.Reunion).filter(
        models.Reunion.id == id
    ).first()

    if reunion is None:
        raise HTTPException(
            status_code=404,
            detail="Reunión no encontrada"
        )

    return reunion


# 4. ACTUALIZAR UNA REUNIÓN
@app.put("/reuniones/{id}", response_model=schemas.ReunionResponse)
def actualizar_reunion(
    id: int,
    datos: schemas.ReunionCreate,
    db: Session = Depends(get_db)
):

    reunion = db.query(models.Reunion).filter(
        models.Reunion.id == id
    ).first()

    if reunion is None:
        raise HTTPException(
            status_code=404,
            detail="Reunión no encontrada"
        )

    for campo, valor in datos.model_dump().items():
        setattr(reunion, campo, valor)

    db.commit()
    db.refresh(reunion)

    return reunion


# 6. ELIMINAR UNA REUNIÓN
@app.delete("/reuniones/{id}")
def eliminar_reunion(id: int, db: Session = Depends(get_db)):

    reunion = db.query(models.Reunion).filter(
        models.Reunion.id == id
    ).first()

    if reunion is None:
        raise HTTPException(
            status_code=404,
            detail="Reunión no encontrada"
        )

    db.delete(reunion)
    db.commit()

    return {"mensaje": "Reunión eliminada correctamente"}
