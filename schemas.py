from pydantic import BaseModel
from datetime import date, time


class ReunionCreate(BaseModel):
    titulo: str
    descripcion: str
    fecha: date
    hora: time
    lugar: str
    responsable: str


class ReunionResponse(ReunionCreate):
    id: int

    class Config:
        from_attributes = True